from pymongo import MongoClient


def get_mongo():
    client = MongoClient('mongodb://localhost')
    db = client.WEBHW10

    return db
