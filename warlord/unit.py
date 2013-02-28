class ItemNotInInventoryError(LookupError):
    pass

class Unit(object):
    def __init__(self):
        self.location = (0, 0)
        self.level = 1
        self.experience = 0
        self._health = 0
        self.max_health = 0
        self.speed = 0
        self.strength = 0
        self.inventory = []
        self.equipped_item = None

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = min(max(value, 0), self.max_health)

    def damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def equip_item(self, item):
        if item not in self.inventory:
            raise ItemNotInInventoryError
        self.equipped_item = item

    def is_passible(self, tile):
        raise NotImplementedError

    def is_visible(self, tile):
        raise NotImplementedError

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

def calculate_damage(unitA, unitB):
    return max(unitA.strength, 0)

def calculate_attack_count(unitA, unitB):
    return max(unitA.speed - unitB.speed + 1, 1)

def combat(unitA, unitB):
    units = (unitA, unitB)
    attack_counts = (calculate_attack_count(unitA, unitB),
                     calculate_attack_count(unitB, unitA))

    unit_num = 0
    while any([c > 0 for c in attack_counts]) and all([u.health > 0 for u in
            units]):
        attacker = units[unit_num]
        defender = units[(unit_num + 1) % 2]
        defender.damage(calculate_damage(attacker, defender))
        attack_counts = ((attack_counts[0] if unit_num == 1 else
                attack_counts[0] - 1), (attack_counts[1] if unit_num == 0 else
                    attack_counts[1] - 1))
        if attack_counts[(unit_num + 1) % 2] > 0:
            unit_num = (unit_num + 1) % 2
