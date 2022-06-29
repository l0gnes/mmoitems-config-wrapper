from ..abc.DropTableRecord import DropTableRecord

class DeconstructionChance(object):

    success : DropTableRecord
    lose: DropTableRecord

    def __init__(
        self,
        success : DropTableRecord,
        lose: DropTableRecord
    ):
        self.success = success
        self.lose = lose

    def toJSON(self):
        return {
            "success" : self.success.toJSON(),
            "lose" : self.lose.toJSON()
        }