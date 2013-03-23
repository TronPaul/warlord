from unittest import TestCase
from mock import Mock, PropertyMock

class MockTile(object):
    def __init__(self):
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self.unit = None

    @property
    def up(self):
        if not self._up:
            self._up = MockTile()
        return self._up

    @property
    def down(self):
        if not self._down:
            self._down = MockTile()
        return self._down

    @property
    def left(self):
        if not self._left:
            self._left = MockTile()
        return self._left

    @property
    def right(self):
        if not self._right:
            self._right = MockTile()
        return self._right

class TestPath(TestCase):
    def setUp(self):
        self.unit = Mock()
        self.tile = MockTile()
        self.unit.tile = self.tile
        self.tile.unit = self.unit

    def test_distance(self):
        from warlord.path import distance
        tileA = Mock()
        tileB = Mock()
        tileA.location = (0, 0)
        tileB.location = (0, 1)
        self.assertEquals(distance(tileA, tileB), 1)

    def test_path_up(self):
        from warlord.path import path
        path(self.unit, ('U',))
        self.assertEqual(self.unit.tile, self.tile.up)
        self.assertEqual(self.tile.up.unit, self.unit)

    def test_path_down(self):
        from warlord.path import path
        path(self.unit, ('D',))
        self.assertEqual(self.unit.tile, self.tile.down)
        self.assertEqual(self.tile.down.unit, self.unit)

    def test_path_left(self):
        from warlord.path import path
        path(self.unit, ('L',))
        self.assertEqual(self.unit.tile, self.tile.left)
        self.assertEqual(self.tile.left.unit, self.unit)

    def test_path_right(self):
        from warlord.path import path
        path(self.unit, ('R',))
        self.assertEqual(self.unit.tile, self.tile.right)
        self.assertEqual(self.tile.right.unit, self.unit)

    def test_path_bad_direction(self):
        from warlord.path import path, BadDirectionError
        self.assertRaises(BadDirectionError, path, self.unit, ('X',))

    def test_multi_direction_path(self):
        from warlord.path import path
        path(self.unit, ('U', 'U', 'L', 'L', 'D', 'R', 'D', 'L', 'U'))
        new_tile = self.tile.up.up.left.left.down.right.down.left.up
        self.assertEquals(self.unit.tile, new_tile)
        self.assertEqual(new_tile.unit, self.unit)

    def test_path_with_impassible_square(self):
        from warlord.path import path, ImpassibleTileError
        tile = Mock()
        self.unit.is_passible.return_value = False
        self.assertRaises(ImpassibleTileError, path, self.unit, ('U',))

    def test_check_path_up(self):
        from warlord.path import check_path
        self.assertTrue(check_path(self.unit, ('U',), self.tile))

    def test_check_path_down(self):
        from warlord.path import check_path
        self.assertTrue(check_path(self.unit, ('D',), self.tile))

    def test_check_path_left(self):
        from warlord.path import check_path
        self.assertTrue(check_path(self.unit, ('L',), self.tile))

    def test_check_path_right(self):
        from warlord.path import check_path
        self.assertTrue(check_path(self.unit, ('R',), self.tile))

    def test_check_step_up(self):
        from warlord.path import check_step
        self.assertTrue(check_step(self.unit, 'U', self.tile))

    def test_check_step_down(self):
        from warlord.path import check_step
        self.assertTrue(check_step(self.unit, 'D', self.tile))

    def test_check_step_left(self):
        from warlord.path import check_step
        self.assertTrue(check_step(self.unit, 'L', self.tile))

    def test_check_step_right(self):
        from warlord.path import check_step
        self.assertTrue(check_step(self.unit, 'R', self.tile))

    def test_check_step_with_bad_direction(self):
        from warlord.path import check_step, BadDirectionError
        self.assertRaises(BadDirectionError, check_step, self.unit, ('X',), self.tile)

    def test_check_path_with_bad_direction(self):
        from warlord.path import check_path, BadDirectionError
        self.assertRaises(BadDirectionError, check_path, self.unit, ('X',), self.tile)

    def test_check_step_with_impassible_square(self):
        from warlord.path import check_step
        self.unit.is_passible.return_value = False
        self.assertTrue(not check_step(self.unit, 'U', self.tile))

    def test_check_step_with_visibility(self):
        from warlord.path import check_step
        self.unit.is_passible.return_value = False
        self.unit.is_visible.return_value = False
        self.assertTrue(check_step(self.unit, 'U', self.tile,
            ignore_visibility=True))

    def test_check_multi_direction_path(self):
        from warlord.path import check_path
        self.assertTrue(check_path(self.unit,
            ('U', 'U', 'L', 'L', 'D', 'R', 'D', 'L', 'U'), self.tile))

    def test_check_path_with_impassible_square(self):
        from warlord.path import check_path, ImpassibleTileError
        tile = Mock()
        self.unit.is_passible.return_value = False
        self.assertTrue(not check_path(self.unit, ('U',), tile))

    def test_check_path_with_visibility(self):
        from warlord.path import check_path
        tile = Mock()
        self.unit.is_passible.return_value = False
        self.unit.is_visible.return_value = False
        self.assertTrue(check_path(self.unit, ('U',), tile,
            ignore_visibility=True))
