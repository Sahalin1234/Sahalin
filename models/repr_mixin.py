

class ReprMixin:
    def __repr__(self):
        attrs = ", ".join(repr(value) for value in self.__dict__.values())
        return f"{self.__class__.__name__}({attrs})"
