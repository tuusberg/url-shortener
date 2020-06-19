from json import dumps
from aiohttp import web
from app.url_shortener import UrlShortener
from pymongo.errors import DuplicateKeyError


class RequestHandler:
    def __init__(self, db_client):
        self.db_client = db_client
        self.db_collection = self.db_client['url-shortener']['urls']

    async def shorten_url(self, request: web.Request):
        body = await request.json()
        if 'url' not in body:
            raise web.HTTPInternalServerError

        url = body['url']
        key = UrlShortener.shorten(url)

        document = {
            '_id': key,
            'originalURL': url,
        }

        try:
            await self.db_collection.insert_one(document)
        except DuplicateKeyError:
            pass

        return web.Response(body=dumps(document), content_type='application/json')

    async def redirect(self, request: web.Request):
        key = request.match_info['key']

        url = await self.db_collection.find_one(key)
        url = url['originalURL'] if url else None

        if url:
            return web.Response(status=302, headers={
                'Connection': 'close',
                'Location': url
            })
        else:
            raise web.HTTPNotFound
