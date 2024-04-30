#!/usr/bin/env python3
''' find '''


def schools_by_topic(mongo_collection, topic):
    ''' topics find '''
    calls = mango_collection.find({"topics": topic})
    return list(calls)
