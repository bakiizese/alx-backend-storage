#!/usr/bin/env python3
'''redis 00'''
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        ''' convo '''
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        ''' return str '''
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key: str) -> int:
        ''' int return '''
        val = self.redis.get(key)
        try:
            val = int(value.decode('utf-8'))
        except Exception:
            val = 0
        return vl
