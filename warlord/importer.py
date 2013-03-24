class BadUnitAttributeError(LookupError):
    pass

def import_map(tile_num_map, tile_factory_list):
    tile_map = []
    for i, tile_num_row in enumerate(tile_num_map):
        tile_row = []
        tile_map.append(tile_row)
        for j, tile_num in enumerate(tile_num_row):
            tile = tile_factory_list[tile_num]()
            print tile
            print (j, -i)
            tile.location = (j, -i)
            if i > 0:
                tile.up = tile_map[i-1][j]
                tile.up.down = tile
            if j > 0:
                tile.left = tile_map[i][j-1]
                tile.left.right = tile
            tile_row.append(tile)
    return tile_map

def import_tile_factory(tile_defn):
    from warlord.tile import Tile
    def tile_factory():
        tile = Tile()
        tile.type = tile_defn['type']
        return tile
    return tile_factory

def import_unit(unit_defn):
    from warlord.unit import Unit
    unit = Unit()
    items = unit_defn.pop('items', [])
    if items:
        pass
    equipped_item = unit_defn.pop('equipped_item', None)
    if equipped_item:
        pass
    attrs = unit_defn.keys()
    def attr_cmp(x, y):
        if x.startswith('max_') or x.startswith('min_'):
            if y.startswith('max_') or y.startswith('min_'):
                return cmp(x, y)
            else:
                return -1
        else:
            if y.startswith('max_') or y.startswith('min_'):
                return 1
            else:
                return cmp(x, y)
    attrs = sorted(attrs, attr_cmp)
    for attr in attrs:
        val = unit_defn[attr]
        if not hasattr(unit, attr):
            raise BadUnitAttributeError
        setattr(unit, attr, val)
    return unit
