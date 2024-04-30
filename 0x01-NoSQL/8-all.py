#!/usr/bin/env python3
''' list all '''


def list_all(mongo_collection):
    ''' all '''
    documents = mongo_collection.find()

    if documnets.count() == 0:
        return []

    return documents
