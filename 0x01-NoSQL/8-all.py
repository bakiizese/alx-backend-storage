#!/usr/bin/env python3
'''all'''


def list_all(mongo_collection):
    '''list all'''
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
