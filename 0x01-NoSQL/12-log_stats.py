#!/usr/bin/env python3
''' pymongo '''
from pymongo import MongoClient


if __name__ == "__main__":
    ''' connect '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    st = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f'{st} status check')
