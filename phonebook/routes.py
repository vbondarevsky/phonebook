from phonebook.api.handler.blocking import BlockingHandler
from phonebook.api.handler.identification import IdentificationHandler


def setup_routes(app):
    app.add_routes(BlockingHandler().routes)
    app.add_routes(IdentificationHandler().routes)
