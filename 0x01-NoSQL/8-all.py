#!/usr/bin/env python3
''' list all '''


def list_all(mongo_collection):
    ''' all '''
    documents = mongo_collection.find()

    ls = list(documents)
    if len(ls) == 0:
        return []

    return documents
