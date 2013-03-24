class BadDirectionError(ValueError):
    pass

class ImpassibleTileError(ValueError):
    pass

def distance(tileA, tileB):
    return sum(sum(comb) for comb in zip(tileA.location, tileB.location))

def path(unit, path):
    tile = unit.tile
    for step in path:
        if not check_step(unit, step, tile):
            raise ImpassibleTileError
        if step == 'U':
            tile = tile.up
        elif step =='D':
            tile = tile.down
        elif step == 'R':
            tile = tile.right
        elif step =='L':
            tile = tile.left
    tile.unit = unit
    unit.tile = tile

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
