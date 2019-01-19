import logging
import logging.config
import optparse
import os

import aiohttp.web
import yaml

from phonebook import config
from phonebook.db.connect import close_db
from phonebook.db.connect import open_db
from phonebook.middleware.basic_auth import basic_auth
from phonebook.routes import setup_routes


def setup_logging():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, "logger.yml")) as f:
        logging_settings = yaml.safe_load(f)
    logging.config.dictConfig(logging_settings)


def run_server():
    app = aiohttp.web.Application(middlewares=[basic_auth])
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
    setup_logging()
    run_server()


if __name__ == "__main__":
    run()
