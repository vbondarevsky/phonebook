from phonebook.config.base_config import BaseConfig


class DbConfig(BaseConfig):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name={self.name}"
