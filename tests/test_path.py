from unittest import TestCase
from mock import Mock, PropertyMock

class TestPath(TestCase):
    def setUp(self):
        self.unit = Mock()
        self.unit.location = (0, 0)
        self.tile = self._makeMockTile()

    def _makeMockTile(self):
        tile = Mock()
        tilegen = PropertyMock(side_effect=self._makeMockTile)
        type(tile).up = tilegen
        type(tile).down = tilegen
        type(tile).left = tilegen
        type(tile).right = tilegen
        type(tile).impassible = PropertyMock(return_value=False)
        return tile

    def test_path_up(self):
        from warlord.path import path
        path(self.unit, ('U',), self.tile)
        self.assertEqual(self.unit.location, (0, 1))

    def test_path_down(self):
        from warlord.path import path
        path(self.unit, ('D',), self.tile)
        self.assertEqual(self.unit.location, (0, -1))

    def test_path_left(self):
        from warlord.path import path
        path(self.unit, ('L',), self.tile)
        self.assertEqual(self.unit.location, (-1, 0))

    def test_path_right(self):
        from warlord.path import path
        path(self.unit, ('R',), self.tile)
        self.assertEqual(self.unit.location, (1, 0))

    def test_path_bad_direction(self):
        from warlord.path import path, BadDirectionError
        self.assertRaises(BadDirectionError, path, self.unit, ('X',), self.tile)

    def test_multi_direction_path(self):
        from warlord.path import path
        path(self.unit, ('U', 'U', 'L', 'L', 'D', 'R', 'D', 'L', 'U'),
                self.tile)
        self.assertTrue(self.unit.location, (-2, 1))

    def test_path_with_impassible_square(self):
        from warlord.path import path, ImpassibleTileError
        tile = Mock()
        self.unit.is_passible.return_value = False
        self.assertRaises(ImpassibleTileError, path, self.unit, ('U',), tile)

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
