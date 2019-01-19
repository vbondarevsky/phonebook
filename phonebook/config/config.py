import yaml

from phonebook.config.api_config import ApiConfig
from phonebook.config.db_config import DbConfig

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, path="", source=""):
        self._load(path, source)

    def __str__(self):
        return f"api: {self.api}"

    def reload(self, path="", source=""):
        self._load(path, source)

    def _load(self, path, source):
        config = self._config(path, source)

        self.api = self._api_config(config)
        self.db = self._db_config(config)

    @staticmethod
    def _api_config(config):
        host = "localhost"
        port = 9797
        if "api" in config:
            if "host" in config["api"]:
                host = config["api"]["host"]
            if "port" in config["api"]:
                port = config["api"]["port"]
        return ApiConfig(host, port)

    @staticmethod
    def _db_config(config):
        name = ""
        if "db" in config:
            name = config["db"]["name"]
        return DbConfig(name)

    @staticmethod
    def _config(path, source):
        if source:
            config = yaml.load(source, Loader)
        elif path:
            with open(path) as f:
                config = yaml.load(f, Loader)
        else:
            config = {}

        return config
