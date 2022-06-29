from ..enums.Color import Color

__all__ = ["ItemGlow"]

class ItemGlow(object):
    
    def __init__(
        self,
        hint : bool,
        color : Color
    ):
        self.color = color
        self.hint = hint

    def toJSON(self) -> dict:
        return {
            "color" : self.color.name,
            "hint" : self.hint
        }