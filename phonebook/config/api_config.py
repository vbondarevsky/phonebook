from phonebook.config.base_config import BaseConfig


class ApiConfig(BaseConfig):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __str__(self):
        return f"host={self.host}, port={self.port}"
