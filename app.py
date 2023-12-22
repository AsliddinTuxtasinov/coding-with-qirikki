import os
from slugify import slugify
from flask import Flask, request, render_template

app = Flask(__name__)


def get_articles():
    articles = os.listdir("articles")
    slug_article = {}

    for article in articles:
        slug = slugify(article)
        slug_article[slug] = article

    return slug_article


@app.route('/')
def home():
    articles = get_articles()
    return render_template("index.html", articles=articles)


@app.route('/blog/<slug>')
def blog_detail(slug: str):
    articles = get_articles()

    try:
        title = articles[slug]
    except Exception as e:
        print(f"Error: {e}")
        return f"Object not found"

    with open(f"articles/{title}") as f:
        content = f.read()

    return render_template("article-detail.html", title=title, content=content)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template('add.html')

    if request.method == 'POST':
        a = int(request.form.get('a', 0))
        b = int(request.form.get('b', 0))

        summ = a + b
        return render_template('add.html', summ=summ)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
