from unittest import TestCase
from mock import Mock

class TestWeapon(TestCase):
    def setUp(self):
        from warlord.weapon import Weapon
        self.weapon = Weapon()

    def test_default_weight(self):
        self.assertEquals(self.weapon.weight, 0)

    def test_default_accuracy(self):
        self.assertEquals(self.weapon.accuracy, 0)

    def test_default_might(self):
        self.assertEquals(self.weapon.might, 0)

    def test_default_countered_weapon_types(self):
        self.assertEquals(self.weapon.countered_weapon_types, [])

    def test_default_countered_by_weapon_types(self):
        self.assertEquals(self.weapon.countered_by_weapon_types, [])

    def test_default_countered_unit_types(self):
        self.assertEquals(self.weapon.countered_unit_types, [])

    def test_default_countered_by_unit_types(self):
        self.assertEquals(self.weapon.countered_by_unit_types, [])

    def test_weapon_counter_bonus_raises_not_implemented(self):
        self.assertRaises(NotImplementedError, self.weapon.weapon_counter_bonus,
                Mock())

    def test_unit_counter_raises_not_implemented(self):
        self.assertRaises(NotImplementedError, self.weapon.unit_counter_bonus,
                Mock())
