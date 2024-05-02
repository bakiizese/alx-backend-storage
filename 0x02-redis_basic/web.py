#!/usr/bin/env python3
''' web '''

import redis
from functools import wraps
import requests
from typing import Callable

rediss = redis.Redis()


def count_req(met: Callable) -> Callable:
    ''' counts '''
    @wraps(met)
    def wrapper(url):
        ''' wrapper '''
        rediss.incr(f"count:{url}")
        cached = rediss.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        html = met(url)
        rediss.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_req
def get_page(url: str) -> str:
    ''' return count tx '''
    rq = requests.get(url)
    return rq.text
