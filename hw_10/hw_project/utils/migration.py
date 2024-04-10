import os
import django
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author # noqa

uri = "mongodb+srv://user_m8:567234@yarval.aryslwo.mongodb.net/?retryWrites=true&w=majority&appName=Yarval"

client = MongoClient(uri)
db = client.module8
authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
    fullname = author['fullname'],
    born_date = author['born_date'],
    born_location = author['born_location'],
    description = author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in (quote['tags']):
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(quote=quote['quote'], author=a)

        for tag in tags:
            q.tags.add(tag)





