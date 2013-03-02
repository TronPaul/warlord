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

    def test_trinity_bonus_raises_not_implemented(self):
        self.assertRaises(NotImplementedError, self.weapon.trinity_bonus,
                Mock())
