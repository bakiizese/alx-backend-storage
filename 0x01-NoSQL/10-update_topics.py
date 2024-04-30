#!/usr/bin/env python3
'''update pymongo'''


def update_topics(mongo_collection, name, topics):
    '''updates'''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
