from flask import Flask, render_template, make_response, session, request, redirect

from article import Article
from conf.utils import USERS, check_password

app = Flask(__name__)

# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = "ThisIsTheSecretKey"


# Learning cookies
@app.route("/first-time")
def first_time():
    if request.cookies.get("seen") is None:
        response = make_response(f"You have registered to cookie !")
        response.set_cookie("seen", "1")
        return response

    seen_times = request.cookies.get("seen")
    response = make_response(f"you are already seen {seen_times} times")
    response.set_cookie("seen", str(int(seen_times) + 1))
    return response


# Learning sessions
@app.route("/learning-sessions")
def learning_sessions():
    if session.get("user") is None:
        session.setdefault("user", "Asil bro")
        return f"You have registered to session !"

    user = session.get("user")
    return f"session user is  {user} !"


@app.route("/")
def home():
    articles = Article.all()
    return render_template("index.html", articles=articles)


@app.route("/blog/<slug>")
def blog_detail(slug: str):
    articles = Article.all()

    try:
        article = articles[slug]
    except Exception as e:
        print(f"Error: {e}")
        return f"Object not found"

    return render_template("article-detail.html", article=article)


# Login section part one
@app.get("/login")
def login_page():
    return render_template("login.html")


# Login section part two
@app.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if USERS.get(username) is None:
        return render_template("login.html", errors="username or password is invalid !")

    hash_password = USERS.get(username)
    if check_password(hash_password=hash_password, password=password):
        del session["user"]
        session.setdefault("user", username)
        return redirect(location="/learning-sessions")

    return render_template("login.html", errors="username or password is invalid !")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
