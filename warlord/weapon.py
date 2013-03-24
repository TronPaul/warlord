from item import Item, LimitedUsesMixin
from combat import calculate_damage

class EquipableItem(Item):
    def __init__(self):
        super(EquipableItem, self).__init__()
        self.weight = 0
        self.accuracy = 0
        self.might = 0
        self.equipable = True

class Staff(LimitedUsesMixin, EquipableItem):
    def __init__(self):
        super(Staff, self).__init__()
        self.base_healing = 0
        self.cast_range = []

    @property
    def healing_amount(self):
        return self.owner.magic + self.might + self.base_healing

    def use(self, target):
        super(Staff, self).use(target)
        target.health += self.healing_amount

class Weapon(LimitedUsesMixin, EquipableItem):
    def __init__(self):
        super(Weapon, self).__init__()
        self.attack_range = []

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
