from item import Item, LimitedUsesMixin
from combat import calculate_damage

class Weapon(LimitedUsesMixin, Item):
    def __init__(self):
        super(Weapon, self).__init__()
        self.weight = 0
        self.accuracy = 0
        self.might = 0
        self.attack_range = []
        self.equipable = True

        self.countered_weapon_types = []
        self.countered_by_weapon_types = []
        self.countered_unit_types = []
        self.countered_by_unit_types = []

    def weapon_counter_bonus(self, weapon_other):
        if weapon_other.type in self.countered_weapon_types:
            return 1
        elif weapon_other.type in self.countered_by_weapon_types:
            return -1
        else:
            return 0

    def unit_counter_bonus(self, unit):
        if unit.type in self.countered_unit_types:
            return 1
        elif unit.type in self.countered_by_unit_types:
            return -1
        else:
            return 0

    def use(self, target):
        super(Weapon, self).use(target)
        target.health -= calculate_damage(self.owner, target)
