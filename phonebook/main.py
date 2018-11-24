import optparse

import aiohttp.web

from phonebook import config
from phonebook.db.connect import close_db
from phonebook.db.connect import open_db
from phonebook.routes import setup_routes


def run_server():
    app = aiohttp.web.Application(debug=config.api.debug)
    setup_routes(app)
    app.on_startup.append(open_db)
    app.on_cleanup.append(close_db)
    aiohttp.web.run_app(app, host=config.api.host, port=config.api.port)


def run():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--config", dest="config", help="path to config file")

    (options, args) = parser.parse_args()

    if options.config:
        config.reload(path=options.config)
    run_server()


if __name__ == "__main__":
    run()
