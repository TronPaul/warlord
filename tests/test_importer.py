from unittest import TestCase
from mock import Mock

class TestImporter(TestCase):
    def test_import_simple_map(self):
        from json import dumps
        from warlord.importer import import_map
        tile_map = [
                [0,1],
                [0,0]]
        tileA_1 = Mock()
        tileA_1.up = None
        tileA_1.down = None
        tileA_1.left = None
        tileA_1.right = None
        tileB_1 = Mock()
        tileB_1.up = None
        tileB_1.down = None
        tileB_1.left = None
        tileB_1.right = None
        tileA_2 = Mock()
        tileA_2.up = None
        tileA_2.down = None
        tileA_2.left = None
        tileA_2.right = None
        tileA_3 = Mock()
        tileA_3.up = None
        tileA_3.down = None
        tileA_3.left = None
        tileA_3.right = None
        tileAs = [tileA_1, tileA_2, tileA_3]
        tileBs = [tileB_1,]
        def tileA_factory(*args, **kwargs):
            return tileAs.pop(0)
        def tileB_factory(*args, **kwargs):
            return tileBs.pop(0)
        tileA_factory_mock = Mock(side_effect=tileA_factory)
        tileB_factory_mock = Mock(side_effect=tileB_factory)
        tile_factory_list = [tileA_factory_mock, tileB_factory_mock]
        tile_map = import_map(tile_map, tile_factory_list)
        self.assertEquals(tile_map, [
            [tileA_1, tileB_1],
            [tileA_2, tileA_3]])
        self.assertEquals(tileA_1.location, (0,0))
        self.assertEquals(tileA_1.down, tileA_2)
        self.assertEquals(tileA_1.right, tileB_1)
        self.assertTrue(tileA_1.up is None)
        self.assertTrue(tileA_1.left is None)
        self.assertEquals(tileB_1.location, (1,0))
        self.assertEquals(tileB_1.down, tileA_3)
        self.assertEquals(tileB_1.left, tileA_1)
        self.assertTrue(tileB_1.up is None)
        self.assertTrue(tileB_1.right is None)
        self.assertEquals(tileA_2.location, (0,-1))
        self.assertEquals(tileA_2.up, tileA_1)
        self.assertEquals(tileA_2.right, tileA_3)
        self.assertTrue(tileA_2.left is None)
        self.assertTrue(tileA_2.down is None)
        self.assertEquals(tileA_3.location, (1,-1))
        self.assertEquals(tileA_3.up, tileB_1)
        self.assertEquals(tileA_3.left, tileA_2)
        self.assertTrue(tileA_3.down is None)
        self.assertTrue(tileA_3.right is None)

    def test_import_tile_factory(self):
        from warlord.importer import import_tile_factory
        tile_defn = {
            'type':'plains'
        }
        tile_factory = import_tile_factory(tile_defn)
        tile = tile_factory()
        self.assertEquals(tile.type, 'plains')

    def test_import_simple_item(self):
        from warlord.importer import import_item
        item_defn = {
            'name':'test_item',
            'value':100
        }
        item = import_item(item_defn)
        self.assertEquals(item.name, 'test_item')
        self.assertEquals(item.value, 100)

    def test_import_potion(self):
        from warlord.importer import import_item
        from warlord.item import LimitedUseMixin, StatChangingMixin, Item
        item_defn = {
            'item_type':'limited_use_stat_changing',
            'name':'Potion',
            'value':30,
            'uses':3,
            'stats':{
                'health':10
            }
        }
        item = import_item(item_defn)
        self.assertTrue(isinstance(item, LimitedUseMixin))
        self.assertTrue(isinstance(item, StatChangingMixin))
        self.assertTrue(isinstance(item, Item))
        self.assertEquals(item.name, 'Potion')
        self.assertEquals(item.value, 30)
        self.assertEquals(item.uses, 3)
        self.assertEquals(len(item.stats), 1)
        self.assertEquals(item.stats['health'], 10)

    def test_import_simple_weapon(self):
        from warlord.importer import import_item
        from warlord.weapon import Weapon
        item_defn = {
                'item_type':'weapon',
                'might':1,
                'weight':10,
                'name':'Stabby',
                'value':1000,
                'attack_range':[0],
                'countered_weapon_types':['axe'],
                'countered_by_weapon_types':['lance'],
                'countered_unit_types':['wyvern'],
                'countered_by_unit_types':['pony'],
                'type':'sword',
                'uses':30
        }
        item = import_item(item_defn)
        self.assertTrue(isinstance(item, Weapon))
        self.assertEquals(item.name, 'Stabby')
        self.assertEquals(item.value, 1000)
        self.assertEquals(item.uses, 30)
        self.assertEquals(item.might, 1)
        self.assertEquals(item.weight, 10)
        self.assertEquals(item.type, 'sword')
        self.assertEquals(item.attack_range, [0])
        self.assertEquals(item.countered_weapon_types, ['axe'])
        self.assertEquals(item.countered_by_weapon_types,
                ['lance'])
        self.assertEquals(item.countered_unit_types, ['wyvern'])
        self.assertEquals(item.countered_by_unit_types, ['pony'])

    def test_import_simple_unit(self):
        from warlord.importer import import_unit
        unit_defn = {
            'level':2,
            'experience':1,
            'passable_tile_types':[],
            'critical':1,
            'max_health':1,
            'health':1,
            'strength':1,
            'magic':1,
            'speed':1,
            'luck':1,
            'skill':1,
            'defense':1,
            'resistance':1
        }
        unit = import_unit(unit_defn)
        self.assertEquals(unit.level, 2)
        self.assertEquals(unit.experience, 1)
        self.assertEquals(unit.inventory, [])
        self.assertEquals(unit.equipped_item, None)
        self.assertEquals(unit.passable_tile_types, [])
        self.assertEquals(unit.critical, 1)
        self.assertEquals(unit.max_health, 1)
        self.assertEquals(unit.health, 1)
        self.assertEquals(unit.strength, 1)
        self.assertEquals(unit.magic, 1)
        self.assertEquals(unit.speed, 1)
        self.assertEquals(unit.luck, 1)
        self.assertEquals(unit.skill, 1)
        self.assertEquals(unit.defense, 1)
        self.assertEquals(unit.resistance, 1)
