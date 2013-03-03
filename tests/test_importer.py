from unittest import TestCase
from mock import Mock

class TestImporter(TestCase):
    def test_import_simple_map(self):
        from json import dumps
        from warlord.importer import import_map
        tile_map_json = dumps([
                [0,1],
                [0,0]])
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
        tile_map = import_map(tile_map_json, tile_factory_list)
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
        from json import dumps
        from warlord.importer import import_tile_factory
        tile_defn_json = dumps({
            'type':'plains'
            })
        tile_factory = import_tile_factory(tile_defn_json)
        tile = tile_factory()
        self.assertEquals(tile.type, 'plains')
