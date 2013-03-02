from unittest import TestCase

class TestWeapon(TestCase):
    def setUp(self):
        from warlord.weapon import Weapon
        self.weapon = Weapon()

    def test_default_weight(self):
        self.assertEquals(self.weapon.weight, 0)

    def test_default_accuracy(self):
        self.assertEquals(self.weapon.accuracy, 0)
