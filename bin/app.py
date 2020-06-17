#!/usr/bin/env python3

import os
import sys

_project_dir = os.path.join(os.path.dirname(__file__), os.pardir)

sys.path.insert(0, _project_dir)
from app import Server, RequestHandler
sys.path.pop(0)

from motor.motor_asyncio import AsyncIOMotorClient


if __name__ == '__main__':
    mongo_db_client = AsyncIOMotorClient('localhost', 27017, username='root', password='6sKBDrBTbT')
    domain = 'http://0.0.0.0:8080'
    handler = RequestHandler(mongo_db_client, domain)
    server = Server(handler)
    server.serve()
