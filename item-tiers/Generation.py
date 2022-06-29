# TODO: See if this is used anywheres else and if so move it into the abc folder

from ..abc.AdvancedAttribute import AdvancedScaledAttribute

__all__ = [
    "TierGeneration"
]

class TierGeneration(object):

    chance: float
    capacity : AdvancedScaledAttribute

    def __init__(
        self,
        chance : float,
        capacity : AdvancedScaledAttribute
    ):
        self.chance = chance
        self.capacity = capacity

    def toJSON(self) -> dict:
        return {
            "chance" : self.chance,
            "capacity" : self.capacity.toJSON()
        }