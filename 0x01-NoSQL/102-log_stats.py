#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print(f"{(n_logs := nginx_collection.count_documents({}))} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {(count := count)}")
    status_check_query = {'method': 'GET', 'path': '/status'}
    status_check = nginx_collection.count_documents(status_check_query)
    print(f"{status_check} status check")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}}
    ])
    print("IPs:")
    for top_ip in top_ips:
        print(f"\t{top_ip['ip']}: {top_ip['count']}")
