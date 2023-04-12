#!/usr/bin/env python3
"""
from pymongo import MongoClient
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection. Returns an empty list if there are no documents.
    """
    return [doc for doc in mongo_collection.find()]
