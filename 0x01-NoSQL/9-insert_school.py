#!/usr/bin/env python3
'''insert to a collection'''


def insert_school(mongo_collection, **kwargs):
    '''insert'''
    return mongo_collection.insert(kwargs)
