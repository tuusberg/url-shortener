from aiohttp import web


class Server:
    def __init__(self, request_handler):
        if not request_handler:
            raise ValueError('request_handler argument is missing')

        self.handler = request_handler

    def serve(self):
        app = web.Application()

        app.router.add_get('/{key}', self.handler.redirect)
        app.router.add_post('/', self.handler.shorten_url)

        web.run_app(app)
