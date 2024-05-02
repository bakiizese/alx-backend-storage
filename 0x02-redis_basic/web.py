#!/usr/bin/env python3
''' web '''
import redis
import requests
from functools import wraps
from typing import Callable

rediss = redis.Redis()


def count_requests(method: Callable) -> Callable:
    ''' counts '''
    @wraps(method)
    def wrapper(url):
        ''' wrap '''
        redis.incr(f"count:{url}")
        cached = redis.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        html = method(url)
        redis.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    ''' return count '''
    requestss = requests.get(url)
    return requestss.text
