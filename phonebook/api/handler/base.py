class BaseHandler:
    @property
    def base(self):
        return "/api/v1/contacts"

    def build_route(self, path):
        return self.base + path
