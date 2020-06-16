#!/usr/bin/env python3

import os
import sys

_project_dir = os.path.join(os.path.dirname(__file__), os.pardir)

sys.path.insert(0, _project_dir)
from app import Server, RequestHandler
sys.path.pop(0)


if __name__ == '__main__':
    domain = 'http://0.0.0.0:8080'
    handler = RequestHandler(domain)
    server = Server(handler)
    server.serve()
