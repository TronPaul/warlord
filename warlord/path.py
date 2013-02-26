class BadDirectionError(ValueError):
    pass

class ImpassibleTileError(ValueError):
    pass

def check_step(unit, step, tile):
    if step == 'U':
        return unit.is_passible(tile.up)
    elif step == 'D':
        return unit.is_passible(tile.down)
    elif step == 'R':
        return unit.is_passible(tile.right)
    elif step == 'L':
        return unit.is_passible(tile.left)
    else:
        raise BadDirectionError

def path(unit, path, tile):
    for step in path:
        loc = unit.location
        if not check_step(unit, step, tile):
            raise ImpassibleTileError
        if step == 'U':
            unit.location = (loc[0], loc[1] + 1)
            tile = tile.up
        elif step =='D':
            unit.location = (loc[0], loc[1] - 1)
            tile = tile.down
        elif step == 'R':
            unit.location = (loc[0] + 1, loc[1])
            tile = tile.right
        elif step =='L':
            unit.location = (loc[0] - 1, loc[1])
            tile = tile.left

def check_path(unit, path, tile):
    for step in path:
        if not check_step(unit, step, tile):
            return False
        if step == 'U':
            tile = tile.up
        elif step == 'D':
            tile = tile.down
        elif step == 'R':
            tile = tile.right
        elif step == 'L':
            tile = tile.left
    return True
