from .MMOItemTemplate import MMOItem

__all__ = [
    "DropTableRecord"
]

class DropTableRecord(object):
    coefficient : int
    item : MMOItem

    def __init__(
        self,
        coefficient : int,
        item : MMOItem
    ):
        self.coefficient = coefficient
        self.item = item


    def toJSON(self):
        return {
            "coef" : self.coefficient,
            "items": self.item.generateDropTableInstance()
        }