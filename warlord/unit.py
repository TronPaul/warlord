from stat import HasStats
from effect import HasEffects

class ItemNotInInventoryError(LookupError):
    pass

class ItemNotEquipableError(ValueError):
    pass

class Unit(HasStats, HasEffects):
    def __init__(self):
        super(Unit, self).__init__()
        self.tile = None
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.equipped_item = None
        self.passable_tile_types = []

        self.critical = 0
        self.add_stat('health', min_value=0, max_value=0)
        self.add_stat('strength')
        self.add_stat('magic')
        self.add_stat('speed')
        self.add_stat('luck')
        self.add_stat('skill')
        self.add_stat('defense')
        self.add_stat('resistance')

    @property
    def hit_rate(self):
        return self.equipped_item.accuracy + self.skill * 2 + self.luck

    @property
    def evade(self):
        return self.speed * 2 + self.luck

    @property
    def magical_defense_power(self):
        return self.resistance

    @property
    def physical_defense_power(self):
        return self.defense

    @property
    def critical_rate(self):
        return (self.equipped_item.critical + int(self.skill / 2) +
            self.critical)

    @property
    def critical_evade(self):
        return self.luck

    def add_item(self, item):
        self.inventory.append(item)
        item.owner = self

    def remove_item(self, item):
        self.inventory.remove(item)
        item.owner = None

    def equip_item(self, item):
        if item not in self.inventory:
            raise ItemNotInInventoryError
        if not item.equipable:
            raise ItemNotEquipableError
        self.equipped_item = item

    def is_passable(self, tile):
        return tile is not None and tile.type in self.passable_tile_types

    def add_experience(self, experience):
        self.experience += experience
        if self.experience >= 100:
            level_diff = (self.experience / 100)
            self.level += level_diff
            for i in range(level_diff):
                self.level_up_stats()
            self.experience = self.experience % 100

    def level_up_stats(self):
        pass
