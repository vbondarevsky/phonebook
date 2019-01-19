import aiohttp.web

from phonebook.api.handler.base import BaseHandler
from phonebook.db.models import Blacklist


class BlockingHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/blocking"), self.list),
            aiohttp.web.post(self.build_route("/blocking"), self.add),
            aiohttp.web.delete(self.build_route("/blocking"), self.delete),
        ]

    async def list(self, request):
        return aiohttp.web.json_response(self.success(Blacklist.list(request.app["db"], request["user_id"])))

    async def add(self, request):
        Blacklist.add(request.app["db"], request["user_id"], (await request.json())["data"])
        return aiohttp.web.json_response(self.success())

    async def delete(self, request):
        Blacklist.delete(request.app["db"], request["user_id"], (await request.json())["data"])
        return aiohttp.web.json_response(self.success())
