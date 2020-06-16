from aiohttp import web
from app.url_shortener import UrlShortener


class RequestHandler:
    def __init__(self, domain):
        self.db = {
            'seed': 1
        }
        self.domain = domain

    async def shorten_url(self, request):
        body = await request.json()
        if 'url' not in body:
            raise web.HTTPInternalServerError

        url = body['url']
        key = UrlShortener.shorten(url)

        # TODO: store the key in the DB
        self.db[key] = url

        # increment the counter
        self.db['seed'] += 1

        return web.Response(text='{}/{}'.format(self.domain, key))

    async def redirect(self, request):
        key = request.match_info['key']
        if key in self.db:
            # TODO: fix Maximum (50) redirects followed when there's no www in the domain name
            return web.HTTPFound(location=key)
        else:
            return web.HTTPNotFound()
