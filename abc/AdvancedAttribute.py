from .ScaledAttribute import ScaledAttribute

__all__ = [
    "AdvancedScaledAttribute"
]

class AdvancedScaledAttribute(ScaledAttribute):

    base : float
    scale : float
    spread : float
    max_spread : float

    def __init__(
        self,
        base : float,
        scale : float,
        spread : float,
        max_spread : float
    ) -> None:
        self.base = base
        self.scale = scale
        self.spread = spread
        self.max_spread

    def toJSON(self) -> dict:
        return {
            "base" : self.base,
            "scale" : self.scale,
            "spread" : self.spread,
            "max-spread" : self.max_spread
        }