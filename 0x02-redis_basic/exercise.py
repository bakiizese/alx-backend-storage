#!/usr/bin/env python3
'''redis 00'''
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        ''' connect '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        ''' returns str key '''
        k = str(uuid.uuid4()) 
        self._redis.set(k, data)
        return k
