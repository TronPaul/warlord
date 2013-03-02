from unittest import TestCase
from mock import Mock

class TestTile(TestCase):
    def setUp(self):
        from warlord.tile import Tile
        self.tile = Tile()

    def test_default_location(self):
        self.assertEqual(self.tile.location, (0, 0))

    def test_default_type(self):
        self.assertTrue(self.tile.type is None)

    def test_default_unit(self):
        self.assertTrue(self.tile.unit is None)

    def test_contains(self):
        unit = Mock()
        self.tile.unit = unit
        self.assertTrue(unit in self.tile)
