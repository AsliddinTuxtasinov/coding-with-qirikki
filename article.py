import os

from slugify import slugify


class Article:
    def __init__(self, title):
        self.title = title

    @property
    def slug(self):
        return slugify(self.title)

    @property
    def content(self):
        with open(f"articles/{self.title}") as f:
            content = f.read()
        return content

    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        slug_article = {}

        for title in titles:
            article = Article(title=title)
            slug_article[article.slug] = article

        return slug_article
