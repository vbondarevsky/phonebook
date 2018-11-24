class BaseHandler:
    @property
    def base(self):
        return "/api/v1/contacts"

    def build_route(self, path):
        return self.base + path

    @staticmethod
    def success(data=None):
        result = {"status": "ok"}
        if data:
            result["data"] = data
        return result

    @staticmethod
    def error(err_code, err_text):
        return {
            "status": "error",
            "error": {
                "code": err_code,
                "description": err_text
            }
        }
