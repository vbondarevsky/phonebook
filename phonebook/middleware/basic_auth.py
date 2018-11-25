import aiohttp
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from phonebook.db.models import User


@aiohttp.web.middleware
async def basic_auth(request, handler):
    # TODO: порефакторить
    try:
        username, password, _ = aiohttp.BasicAuth.decode(request.headers["Authorization"])
        user = request.app["db"].query(User).filter_by(name=username).first()
        if user and pbkdf2_sha256.verify(password, user.hash):
            request["user_id"] = user.id
            return await handler(request)
        return aiohttp.web.HTTPUnauthorized()
    except KeyError:
        return aiohttp.web.HTTPUnauthorized()
