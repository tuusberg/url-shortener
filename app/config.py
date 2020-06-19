from os import environ

config = {
    'DB_HOST': environ['URL_SHORTENER_MONGODB_SERVICE_HOST'],
    'DB_PORT': int(environ['URL_SHORTENER_MONGODB_SERVICE_PORT']),
    'DB_USER': 'root',
    'DB_PASS': environ['MONGODB_PASSWORD']
}
