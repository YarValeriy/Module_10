import json
from bson.objectid import ObjectId
from pymongo import MongoClient

uri = "mongodb+srv://user_m8:567234@yarval.aryslwo.mongodb.net/?retryWrites=true&w=majority&appName=Yarval"

client = MongoClient(uri)
db = client.module8

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
    for quote in quotes:
        author = db.authors.find_one({'fullname': quote['author']})
        if author:
            db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
            })