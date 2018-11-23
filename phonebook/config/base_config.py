class BaseConfig:
    def __eq__(self, other):
        return other and str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)
