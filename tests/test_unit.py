from unittest import TestCase

class TestUnit(TestCase):
    def setUp(self):
        from warlord.unit import Unit
        self.unit = Unit()

    def test_default_location(self):
        self.assertEqual(self.unit.location, (0, 0))

    def test_path_up(self):
        from warlord.unit import path
        path(self.unit, ('U',))
        self.assertEqual(self.unit.location, (0, 1))

    def test_path_down(self):
        from warlord.unit import path
        path(self.unit, ('D',))
        self.assertEqual(self.unit.location, (0, -1))

    def test_path_left(self):
        from warlord.unit import path
        path(self.unit, ('L',))
        self.assertEqual(self.unit.location, (-1, 0))

    def test_path_right(self):
        from warlord.unit import path
        path(self.unit, ('R',))
        self.assertEqual(self.unit.location, (1, 0))

    def test_path_bad_direction(self):
        from warlord.unit import path, BadDirectionError
        self.assertRaises(BadDirectionError, path, self.unit, ('X',))

    def test_multi_direction_path(self):
        from warlord.unit import path
        path(self.unit, ('U', 'U', 'L', 'L', 'D', 'R', 'D', 'L', 'U'))
        self.assertTrue(self.unit.location, (-2, 1))

    def test_default_health(self):
        self.assertEquals(self.unit.health, 0)

    def test_damage_vs_unit(self):
        from warlord.unit import calculate_damage
        self.assertEqual(calculate_damage(self.unit, self.unit), 1)

    def test_attack_count_vs_unit(self):
        from warlord.unit import calculate_attack_count
        self.assertEqual(calculate_attack_count(self.unit, self.unit), 1)

    def test_combat(self):
        from warlord.unit import Unit, combat
        unitOther = Unit()
        combat(self.unit, unitOther)
        self.assertEqual(self.unit.health, -1)
        self.assertEqual(unitOther.health, -1)
