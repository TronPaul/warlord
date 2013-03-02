from item import Item, LimitedUsesMixin

class Weapon(LimitedUsesMixin, Item):
    def __init__(self):
        super(Weapon, self).__init__()
        self.weight = 0
        self.accuracy = 0
        self.might = 0
        self.countered_weapon_types = []
        self.countered_by_weapon_types = []
        self.countered_unit_types = []
        self.countered_by_unit_types = []

    def weapon_counter_bonus(self, weapon_other):
        raise NotImplementedError

    def unit_counter_bonus(self, unit):
        raise NotImplementedError
