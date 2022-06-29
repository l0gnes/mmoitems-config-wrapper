from enum import Enum, auto

class MMOItemType(Enum):
    
    # SLASH
    SWORD = auto()

    # PIERCE
    DAGGER = auto()
    SPEAR = auto()

    # BLUNT
    HAMMER = auto()
    GAUNTLET = auto()

    # Range
    WHIP = auto()
    STAFF = auto()
    BOW = auto()
    CROSSBOW = auto()
    MUSKET = auto()
    LUTE = auto()

    # Offhand
    CATALYST = auto()
    OFF_CATALYST = auto()

    # Any
    ORNAMENT = auto()

    # Extra
    ARMOR = auto()
    TOOL = auto()
    CONSUMABLE = auto()
    MISCELLANEOUS = auto()
    GEM_STONE = auto()
    SKIN = auto()
    ACCESSORY = auto()
    BLOCK = auto()
