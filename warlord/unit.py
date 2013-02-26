class Unit(object):
    def __init__(self):
        self.location = (0, 0)

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

