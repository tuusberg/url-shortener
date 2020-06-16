from aiohttp import web
from url_shortener import UrlShortener

routes = web.RouteTableDef()


class Handler:
    def __init__(self):
        self.db = {
            'seed': 1
        }

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

        return web.Response(text='{}/{}'.format('http://0.0.0.0:8080', key))

    async def redirect(self, request):
        key = request.match_info['key']
        if key in self.db:
            # TODO: fix Maximum (50) redirects followed when there's no www in the domain name
            return web.HTTPFound(location=key)
        else:
            return web.HTTPNotFound()


def init_func():
    app = web.Application()

    handler = Handler()
    app.router.add_post('/', handler.shorten_url)
    app.router.add_get('/{key}', handler.redirect)

    web.run_app(app)


if __name__ == '__main__':
    init_func()
