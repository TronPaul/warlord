from json import loads
def import_map(tile_num_map_json, tile_factory_list):
    tile_num_map = loads(tile_num_map_json)
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

def import_tile_factory(tile_defn_json):
    from warlord.tile import Tile
    tile_defn = loads(tile_defn_json)
    def tile_factory():
        tile = Tile()
        tile.type = tile_defn['type']
        return tile
    return tile_factory