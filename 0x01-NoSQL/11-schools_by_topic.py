#!/usr/bin/env python3
'''find'''


def schools_by_topic(mongo_collection, topic):
    '''schoosl'''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
