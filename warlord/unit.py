class Unit(object):
    def __init__(self):
        self.location = (0, 0)
        self.health = 0
        self.speed = 0
        self.strength = 0

class BadDirectionError(ValueError):
    pass

def path(unit, path):
    for step in path:
        loc = unit.location
        if step == 'U':
            unit.location = (loc[0], loc[1] + 1)
        elif step =='D':
            unit.location = (loc[0], loc[1] - 1)
        elif step == 'R':
            unit.location = (loc[0] + 1, loc[1])
        elif step =='L':
            unit.location = (loc[0] - 1, loc[1])
        else:
            raise BadDirectionError

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
        defender.health -= calculate_damage(attacker, defender)
        attack_counts = ((attack_counts[0] if unit_num == 1 else
                attack_counts[0] - 1), (attack_counts[1] if unit_num == 0 else
                    attack_counts[1] - 1))
        if attack_counts[(unit_num + 1) % 2] > 0:
            unit_num = (unit_num + 1) % 2
