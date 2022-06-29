from ..enums.Material import Material
from .Enchantment import AbstractEnchantment
from typing import List, Optional

__all__ = [
    "MMOItem"
]

class MMOItem(object):

    material : Material = Material.STICK
    enchants : Optional[List[AbstractEnchantment]] = []
    hide_enchantments : bool = False
    lore : List[str] = []
    name : str

    def __init__(
        self,
        name : str,
        material : Material,
        *,
        hide_enchantments : bool = False,
        lore : List[str] = [],
        enchants : List[AbstractEnchantment] = []
    ) -> None:
        self.name = name
        self.material = material
        self.hide_enchantments = hide_enchantments
        self.lore = lore
        self.enchants = enchants

    @property
    def has_lore(self):
        return self.lore is not None and len(self.lore) > 0

    @property
    def has_enchantments(self):
        return self.enchants is not None and len(self.enchants) > 0 and all(map(lambda n: n.level > 0, self.enchants))