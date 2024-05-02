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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' returns str key '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
