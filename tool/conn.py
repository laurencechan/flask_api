# coding=utf-8

from flask_pymongo import MongoClient


def mongo_conn():
    client = MongoClient('localhost', 27017)
    db = client["my_flask_api_db"]
    return db
