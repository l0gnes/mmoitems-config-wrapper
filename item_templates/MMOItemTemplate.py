from ..abc.ScaledAttribute import ScaledAttribute
from .ItemTemplateModifier import ItemTemplateModifier
from typing import List

__all__ = [
    "MMOItemTemplate"
]

from enums.Material import Material


class MMOItemTemplate(object):
    
    item_id : str

    # option
    tiered : bool = False
    level_item : bool = False # level-item

    # Base item data:
    material : Material
    name : str
    attack_speed : ScaledAttribute | float = 1.0 # attack-speed
    required_level : ScaledAttribute | int | None = None # required_level

    modifiers : List[ItemTemplateModifier] = []
