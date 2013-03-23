from warlord.path import distance

class UnitOutOfRangeError(ValueError):
    pass

def is_in_range(unitA, unitB):
    dist = distance(unitA.tile, unitB.tile) - 1
    return dist in unitA.equipped_item.attack_range

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
    if not is_in_range(unitA, unitB):
        raise UnitOutOfRangeError
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
