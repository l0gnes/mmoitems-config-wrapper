from ..abc.Material import Material

__all__ = [
    "ItemType"
]

DEFAULT_UNIDENTIFIED_LORE = [
    '&7This item is unidentified. I must',
    '&7find a way to identify it!',
    '{tier}',
    '{tier}&8Item Info:',
    '{range}&8- &7Lvl Range: &e#range#',
    '{tier}&8- &7Item Tier: #prefix##tier#'
]

class ItemType(object):

    display : Material
    name : str

    def toJSON(self) -> dict:
        return {
            self.name.upper() : {
                "display" : Material.tag,
                "name" : self.name,
                "unident-item" : {
                    "name": "&f#prefix#Unidentified %s" % self.name,
                    "lore" : DEFAULT_UNIDENTIFIED_LORE
                }
            }
        }