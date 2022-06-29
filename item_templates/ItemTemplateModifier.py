from .MMOStatistics import MMOStatistics

__all__ = [
    "ItemTemplateModifier"
]

class ItemTemplateModifier(object):
    
    name : str
    prefix : str | None = None
    suffix : str | None = None
    chance : float = None
    stats: MMOStatistics