import aiohttp

from api.handler.base import BaseHandler


class IdentificationHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/identification"), self.list),
            aiohttp.web.post(self.build_route("/identification"), self.add),
        ]

    async def list(self, request):
        return aiohttp.web.json_response({})

    async def add(self, request):
        return aiohttp.web.json_response({})
