class BadDirectionError(ValueError):
    pass

class ImpassibleTileError(ValueError):
    pass

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
