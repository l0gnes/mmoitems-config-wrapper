from .DeconstructionChance import DeconstructionChance
from .Unidentification import Unidentification
from ..abc.ItemGlow import ItemGlow
from .Generation import TierGeneration
from ..enums.Color import Color
from ..util.ConfigBuilder import ConfigBuilder

__all__ = [
    'ItemTier'
]

class ItemTier(object):
    
    name : str
    unidentification : Unidentification         # NOTE: We can automatically allow building this with a classmethod
    generation : TierGeneration

    deconstrucion : DeconstructionChance | None
    item_glow : ItemGlow | None

    def __init__(
        self,
        name : str,
        unidentification : Unidentification,
        generation : TierGeneration,
        *,
        deconstruction : DeconstructionChance | None = None,
        item_glow : ItemGlow | None = None
    ):
        self.name = name
        self.unidentification = unidentification
        self.generation = generation
        self.deconstrucion = deconstruction
        self.item_glow = item_glow

    @classmethod
    def define(
        cls, 
        name : str, 
        unidentification : Unidentification,
        *,
        color : Color = Color.WHITE, 
        deconstruction : DeconstructionChance = None,
        item_glow : bool = False
    ) -> "ItemTier":
        return cls(
            name,
            unidentification = unidentification,
            deconstruction = deconstruction,
            item_glow = ItemGlow(
                item_glow,
                color = color
            )
        )
        
    def toJSON(self) -> dict:
        cb = ConfigBuilder()
        cb.strictAppendConfig("name", self.name)
        cb.strictAppendConfig("unidentification", self.unidentification.toJSON()),
        cb.evalAppendConfig("item-glow", self.item_glow.toJSON(), lambda v: v.hint)
        cb.lenientAppendConfig("deconstruct-item", self.deconstrucion.toJSON())
        return cb.config

