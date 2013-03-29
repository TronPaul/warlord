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

def import_item(item_defn):
    from warlord.item import (LimitedUseMixin, StatChangingMixin,
        LimitedUseStatChangingItem, Item)
    from warlord.weapon import Weapon, EquipableItem
    item_type = item_defn.get('item_type', 'item')
    item_types = {
        'item': Item,
        'limited_use_stat_changing': LimitedUseStatChangingItem,
        'weapon': Weapon
    }
    if item_type not in item_types:
        raise TypeError
    item = item_types[item_type]()
    if isinstance(item, Weapon):
        config_weapon(item, item_defn)
    if isinstance(item, EquipableItem):
        config_equipable_item(item, item_defn)
    if isinstance(item, LimitedUseMixin):
        config_limited_use_item(item, item_defn)
    if isinstance(item, StatChangingMixin):
        config_stat_changing_item(item, item_defn)
    if isinstance(item, Item):
        config_simple_item(item, item_defn)
    return item

def config_equipable_item(item, item_defn):
    if 'weight' in item_defn:
        item.weight = item_defn['weight']
    if 'accuracy' in item_defn:
        item.accuracy = item_defn['accuracy']
    if 'might' in item_defn:
        item.might = item_defn['might']

def config_weapon(item, item_defn):
    if 'attack_range' in item_defn:
        item.attack_range = item_defn['attack_range']
    if 'type' in item_defn:
        item.type = item_defn['type']

    if 'countered_weapon_types' in item_defn:
        item.countered_weapon_types = item_defn['countered_weapon_types']
    if 'countered_by_weapon_types' in item_defn:
        item.countered_by_weapon_types = item_defn['countered_by_weapon_types']
    if 'countered_unit_types' in item_defn:
        item.countered_unit_types = item_defn['countered_unit_types']
    if 'countered_by_unit_types' in item_defn:
        item.countered_by_unit_types = item_defn['countered_by_unit_types']

def config_stat_changing_item(item, item_defn):
    if 'stats' in item_defn:
        item.stats = item_defn['stats']

def config_limited_use_item(item, item_defn):
    if 'uses' in item_defn:
        item.uses = item_defn['uses']

def config_simple_item(item, item_defn):
    from warlord.item import Item
    if 'name' in item_defn:
        item.name = item_defn['name']
    if 'value' in item_defn:
        item.value = item_defn['value']
