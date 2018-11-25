import aiohttp

from phonebook.api.handler.base import BaseHandler
from phonebook.db.models import Contact


class IdentificationHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/identification"), self.list),
            aiohttp.web.post(self.build_route("/identification"), self.add),
        ]

    async def list(self, request):
        return aiohttp.web.json_response(self.success(Contact.list(request.app["db"], request["user_id"])))

    async def add(self, request):
        Contact.add(request.app["db"], request["user_id"], (await request.json())["data"])
        return aiohttp.web.json_response(self.success())
