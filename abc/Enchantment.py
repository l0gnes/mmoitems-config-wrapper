from abc import ABC

class AbstractEnchantment(ABC):
    __max_level : int = 0
    __id : str = "enchantment_id"
    level : int = None

    def __init__(self, level : int, *, unsafe : bool = False) -> None:
    
        if self.__ensureSafeEnchantment(level) and not unsafe:
            self.level = level

        else:
            raise ValueError("Supplied level is higher than this enchantment's highest level")

    def __ensureSafeEnchantment(self, l : int) -> bool:
        return l >= self.__max_level and l > 0

class Sharpness(AbstractEnchantment):
    __max_level = 5
    __id = "sharpness"

class BaneOfArthropods(AbstractEnchantment):
    __max_level = 5
    __id = "bane_of_arthropods"

class AquaAffinity(AbstractEnchantment):
    __max_level = 1
    __id = "aqua_affinity"

class BlastProtection(AbstractEnchantment):
    __max_level = 4
    __id = "blast_protection"

class Channeling(AbstractEnchantment):
    __max_level = 1
    __id = "channeling"

class CurseOfBinding(AbstractEnchantment):
    __max_level = 1
    __id = "binding_curse"

class CurseOfVanishing(AbstractEnchantment):
    __max_level = 1
    __id = "vanishing_curse"

class DepthStrider(AbstractEnchantment):
    __max_level = 3
    __id = "depth_strider"

class Efficiency(AbstractEnchantment):
    __max_level = 5
    __id = "efficiency"

class FeatherFalling(AbstractEnchantment):
    __max_level = 4
    __id = "feather_falling"

class FireAspect(AbstractEnchantment):
    __max_level = 2
    __id = "fire_aspect"

class FireProtection(AbstractEnchantment):
    __max_level = 4
    __id = "fire_protection"

class Flame(AbstractEnchantment):
    __max_level = 1
    __id = "flame"

class Fortune(AbstractEnchantment):
    __max_level = 3
    __id = "fortune"

class FrostWalker(AbstractEnchantment):
    __max_level = 2
    __id = "frost_walker"

class Impaling(AbstractEnchantment):
    __max_level = 5
    __id = "impaling"

class Infinity(AbstractEnchantment):
    __max_level = 1
    __id = "infinity"

class Knockback(AbstractEnchantment):
    __max_level = 2
    __id = "knockback"

class Looting(AbstractEnchantment):
    __max_level = 3
    __id = "looting"

class Loyalty(AbstractEnchantment):
    __max_level = 3
    __id = "loyalty"

class LuckOfTheSea(AbstractEnchantment):
    __max_level = 3
    __id = "luck_of_the_sea"

class Lure(AbstractEnchantment):
    __max_level = 3
    __id = "lure"

class Mending(AbstractEnchantment):
    __max_level = 1
    __id = "mending"

class Multishot(AbstractEnchantment):
    __max_level = 1
    __id = "multishot"

class Piercing(AbstractEnchantment):
    __max_level = 4
    __id = "piercing"

class Power(AbstractEnchantment):
    __max_level = 5
    __id = "power"

class ProjectileProtection(AbstractEnchantment):
    __max_level = 4
    __id = "projecticle_protection"

class Protection(AbstractEnchantment):
    __max_level = 4
    __id = "protection"

class Punch(AbstractEnchantment):
    __max_level = 2
    __id = "punch"

class QuickCharge(AbstractEnchantment):
    __max_level = 3
    __id = "quick_charge"

class Respiration(AbstractEnchantment):
    __max_level = 3
    __id = "respiration"

class Riptide(AbstractEnchantment):
    __max_level = 3
    __id = "riptide"

class SilkTouch(AbstractEnchantment):
    __max_level = 1
    __id = "silk_touch"

class Smite(AbstractEnchantment):
    __max_level = 5
    __id = "smite"

class SoulSpeed(AbstractEnchantment):
    __max_level = 3
    __id = "soul_speed"

class SweepingEdge(AbstractEnchantment):
    __max_level = 3
    __id = "sweeping"

class SwiftSneak(AbstractEnchantment):
    __max_level = 3
    __id = "swift_sneak"

class Thorns(AbstractEnchantment):
    __max_level = 3
    __id = "thorns"
    
class Unbreaking(AbstractEnchantment):
    __max_level = 3
    __id = "unbreaking"

__all__ = [
    Unbreaking,
    Thorns,
    SwiftSneak,
    SoulSpeed,
    Smite,
    SilkTouch,
    Riptide,
    Respiration,
    QuickCharge,
    Punch,
    Protection,
    ProjectileProtection,
    Power,
    Piercing,
    Multishot,
    Lure,
    Mending,
    LuckOfTheSea,
    Loyalty,
    Looting,
    Knockback,
    Infinity,
    Impaling,
    FrostWalker,
    Fortune,
    Flame,
    FireProtection,
    FireAspect,
    FeatherFalling,
    Efficiency,
    DepthStrider,
    CurseOfVanishing,
    CurseOfBinding,
    Channeling,
    BlastProtection,
    BaneOfArthropods,
    AquaAffinity
]