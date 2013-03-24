from unittest import TestCase
from mock import Mock, patch

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

    def test_default_attack_range(self):
        self.assertEquals(self.weapon.attack_range, [])

    def test_default_countered_weapon_types(self):
        self.assertEquals(self.weapon.countered_weapon_types, [])

    def test_default_countered_by_weapon_types(self):
        self.assertEquals(self.weapon.countered_by_weapon_types, [])

    def test_default_countered_unit_types(self):
        self.assertEquals(self.weapon.countered_unit_types, [])

    def test_default_countered_by_unit_types(self):
        self.assertEquals(self.weapon.countered_by_unit_types, [])

    def test_weapon_counter_bonus_with_countered_weapon(self):
        self.weapon.countered_weapon_types.append('axe')
        weaponB = Mock()
        weaponB.type = 'axe'
        self.assertEquals(self.weapon.weapon_counter_bonus(weaponB), 1)

    def test_weapon_counter_bonus_with_uncountered_weapon(self):
        self.weapon.countered_weapon_types.append('axe')
        weaponB = Mock()
        weaponB.type = 'sword'
        self.assertEquals(self.weapon.weapon_counter_bonus(weaponB), 0)

    def test_weapon_counter_bonus_with_countered_by_weapon(self):
        self.weapon.countered_by_weapon_types.append('axe')
        weaponB = Mock()
        weaponB.type = 'axe'
        self.assertEquals(self.weapon.weapon_counter_bonus(weaponB), -1)

    def test_weapon_counter_bonus_with_uncountered_by_weapon(self):
        self.weapon.countered_by_weapon_types.append('axe')
        weaponB = Mock()
        weaponB.type = 'sword'
        self.assertEquals(self.weapon.weapon_counter_bonus(weaponB), 0)

    def test_unit_counter_bonus_with_countered_unit(self):
        self.weapon.countered_unit_types.append('a')
        unit = Mock()
        unit.type = 'a'
        self.assertEquals(self.weapon.unit_counter_bonus(unit), 1)

    def test_unit_counter_bonus_with_uncountered_unit(self):
        self.weapon.countered_unit_types.append('a')
        unit = Mock()
        unit.type = 'b'
        self.assertEquals(self.weapon.unit_counter_bonus(unit), 0)

    def test_unit_counter_bonus_with_countered_by_unit(self):
        self.weapon.countered_by_unit_types.append('a')
        unit = Mock()
        unit.type = 'a'
        self.assertEquals(self.weapon.unit_counter_bonus(unit), -1)

    def test_unit_counter_bonus_with_uncountered_by_unit(self):
        self.weapon.countered_by_unit_types.append('a')
        unit = Mock()
        unit.type = 'b'
        self.assertEquals(self.weapon.unit_counter_bonus(unit), 0)

    @patch('warlord.weapon.calculate_damage')
    def test_use(self, calc_dmg):
        self.weapon.owner = Mock()
        self.weapon.uses = 1
        target = Mock()
        target.health = 1
        calc_dmg.return_value = 1
        self.weapon.use(target)
        self.assertEquals(target.health, 0)
