class BadDirectionError(ValueError):
    pass

class ImpassibleTileError(ValueError):
    pass

def check_step(unit, step, tile):
    if step == 'U':
        return not tile.up.impassible
    elif step == 'D':
        return not tile.down.impassible
    elif step == 'R':
        return not tile.right.impassible
    elif step == 'L':
        return not tile.left.impassible
    else:
        raise BadDirectionError

def path(unit, path, tile):
    for step in path:
        loc = unit.location
        if step == 'U':
            if tile.impassible:
                raise ImpassibleTileError
            unit.location = (loc[0], loc[1] + 1)
            tile = tile.up
        elif step =='D':
            if tile.impassible:
                raise ImpassibleTileError
            unit.location = (loc[0], loc[1] - 1)
            tile = tile.down
        elif step == 'R':
            if tile.impassible:
                raise ImpassibleTileError
            unit.location = (loc[0] + 1, loc[1])
            tile = tile.right
        elif step =='L':
            if tile.impassible:
                raise ImpassibleTileError
            unit.location = (loc[0] - 1, loc[1])
            tile = tile.left
        else:
            raise BadDirectionError

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
        else:
            raise BadDirectionError
        return True

