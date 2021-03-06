#!/usr/bin/env python3

import os
import sys

_project_dir = os.path.join(os.path.dirname(__file__), os.pardir)

sys.path.insert(0, _project_dir)
from app import Server, RequestHandler, config
sys.path.pop(0)

from motor.motor_asyncio import AsyncIOMotorClient


if __name__ == '__main__':
    db_client = AsyncIOMotorClient(config['DB_HOST'], config['DB_PORT'])
    handler = RequestHandler(db_client)
    server = Server(handler)
    server.serve()
