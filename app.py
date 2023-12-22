from flask import Flask, render_template

from article import Article

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
