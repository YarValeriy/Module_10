from pymongo import MongoClient

uri = "mongodb+srv://user_m8:567234@yarval.aryslwo.mongodb.net/?retryWrites=true&w=majority&appName=Yarval"


def get_mongodb():
    client = MongoClient(uri)
    db = client.module8
    return db

