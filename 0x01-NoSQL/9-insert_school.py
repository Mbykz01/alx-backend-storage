#!/usr/bin/env python3
"""9-main
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on keyword arguments.
    Returns the new _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
