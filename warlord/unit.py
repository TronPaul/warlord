from stat import HasStats

class ItemNotInInventoryError(LookupError):
    pass

class Unit(HasStats):
    def __init__(self):
        self.tile = None
        self.team = 0
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

    def remove_item(self, item):
        self.inventory.remove(item)

    def equip_item(self, item):
        if item not in self.inventory:
            raise ItemNotInInventoryError
        self.equipped_item = item

    def is_passable(self, tile):
        return tile is not None and tile.type in self.passable_tile_types

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

def calculate_attack_power(unitA, unitB):
    if unitA.equipped_item.type == 'magical':
        return calculate_magical_attack_power(unitA, unitB)
    elif unitA.equipped_item.type == 'physical':
        return calculate_physical_attack_power(unitA, unitB)

def calculate_magical_attack_power(unitA, unitB):
    weaponA = unitA.equipped_item
    weaponB = unitB.equipped_item
    return base_attack_power(unitA.magic, weaponA.might,
        weaponA.weapon_counter_bonus(weaponB),
        weaponA.unit_counter_bonus(unitB))

def calculate_physical_attack_power(unitA, unitB):
    weaponA = unitA.equipped_item
    weaponB = unitB.equipped_item
    return base_attack_power(unitA.strength, weaponA.might,
        weaponA.weapon_counter_bonus(weaponB),
        weaponA.unit_counter_bonus(unitB))

def base_attack_power(atk_stat, might, weapon_counter, unit_counter):
    return atk_stat + (might + weapon_counter) * (unit_counter + 1)

def calculate_physical_damage(unitA, unitB):
    return max(calculate_physical_attack_power(unitA, unitB) - unitB.defense,
            0)

def calculate_magical_damage(unitA, unitB):
    return max(calculate_magical_attack_power(unitA, unitB) - unitB.resistance,
            0)

def calculate_damage(unitA, unitB):
    if unitA.equipped_item.type == 'magical':
        return calculate_magical_damage(unitA, unitB)
    elif unitA.equipped_item.type == 'physical':
        return calculate_physical_damage(unitA, unitB)

def calculate_attack_count(unitA, unitB):
    dif = unitA.speed - unitB.speed
    return 2 if dif > 3 else 1

def combat(unitA, unitB):
    units = (unitA, unitB)
    attack_counts = (calculate_attack_count(unitA, unitB),
                     calculate_attack_count(unitB, unitA))

    unit_num = 0
    while any([c > 0 for c in attack_counts]) and all([u.health > 0 for u in
            units]):
        attacker = units[unit_num]
        defender = units[(unit_num + 1) % 2]
        defender.health -= calculate_damage(attacker, defender)
        attack_counts = ((attack_counts[0] if unit_num == 1 else
                attack_counts[0] - 1), (attack_counts[1] if unit_num == 0 else
                    attack_counts[1] - 1))
        if attack_counts[(unit_num + 1) % 2] > 0:
            unit_num = (unit_num + 1) % 2
