import aiohttp

from phonebook.api.handler.base import BaseHandler
from phonebook.db.models import Blacklist


class BlockingHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/blocking"), self.list),
            aiohttp.web.post(self.build_route("/blocking"), self.add),
        ]

    async def list(self, request):
        return aiohttp.web.json_response(self.success(Blacklist.list(request.app["db"])))

    async def add(self, request):
        Blacklist.add(request.app["db"], await request.json()["data"])
        return aiohttp.web.json_response(self.success())
