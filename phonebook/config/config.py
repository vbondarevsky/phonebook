import yaml

from phonebook.config.api_config import ApiConfig


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

    @staticmethod
    def _api_config(config):
        host = "localhost"
        port = 9797
        debug = False
        if "api" in config:
            if "host" in config["api"]:
                host = config["api"]["host"]
            if "port" in config["api"]:
                port = config["api"]["port"]
            if "debug" in config["api"]:
                debug = config["api"]["debug"]
        return ApiConfig(host, port, debug)

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
