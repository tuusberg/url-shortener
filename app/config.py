from os import environ

config = {}

config.DB_HOST = 'mongodb.default.svc.cluster.local'
config.DB_PORT = 27017
config.DB_USER = 'root'
config.DB_PASS = environ['MONGODB_PASSWORD']
