from dataclasses import dataclass, asdict
from typing import Union
from .AdvancedAttribute import AdvancedScaledAttribute
from .ScaledAttribute import ScaledAttribute

__all__ = [
    "MMOStatistics"
]

@dataclass
class MMOStatistics():
    
    # Vanilla Attribute Things
    attack_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    attack_speed : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_health : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    movement_speed : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    knockback_resistance : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    armor : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    armor_toughness : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None

    # Resources
    max_mana : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_stamina : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_stellium : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    health_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_health_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    mana_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_mana_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    stellium_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_stellium_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    stamina_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    max_stamina_regeneration : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None

    # Utility
    additional_experience : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    cooldown_reduction : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    speed_malus_reduction : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None

    # Critical Strikes
    critical_strike_chance : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    critical_strike_power : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    skill_critical_strike_chance : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    skill_critical_strike_power : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    
    # Damage Stats
    magic_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    physical_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    projectile_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    weapon_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    skill_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    undead_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    pvp_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None
    pve_damage : Union[AdvancedScaledAttribute, ScaledAttribute, int, None] = None

    def toJSON(self) -> dict:
        d = asdict(self)
        return { k.replace('_', '-') : v for k, v in d.items() if v is not None }