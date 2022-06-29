__all__ = [
    "ScaledAttribute"
]

class ScaledAttribute(object):

    base: float
    scale : float

    def __init__(self, base : float, scale : float) -> None:
        self.scale = scale
        self.base = base

    def toJSON(self) -> dict:
        return {
            "base" : self.base,
            "scale" : self.scale
        }