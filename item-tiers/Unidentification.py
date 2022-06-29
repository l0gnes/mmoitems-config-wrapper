__all__ = [
    "Unidentification"
]

class Unidentification(object):
    
    range : int
    name : str
    prefix : str

    def __init__(
        self,
        name : str,
        prefix : str,
        range : int
    ):
        self.range = range
        self.name = name
        self.prefix = prefix

    def toJSON(self) -> dict:
        return {
            "range" : self.range,
            "name" : self.name,
            "prefix" : self.prefix
        }