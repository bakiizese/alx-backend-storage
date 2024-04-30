#!/usr/bin/env python3
''' find '''


def schools_by_topic(mongo_collection, topic):
    ''' topics find '''
    documents = mango_collection.find({"topics": {'$elemMatch':
                                      {'$eq': topic}}})
    return [d for d in documents]
