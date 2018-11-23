from phonebook.config.base_config import BaseConfig


class ApiConfig(BaseConfig):
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug

    def __str__(self):
        return f"host={self.host}, port={self.port}, debug={self.debug}"
