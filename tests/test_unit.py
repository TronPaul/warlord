from unittest import TestCase

class TestUnit(TestCase):
    def setUp(self):
        from warlord.unit import Unit
        self.unit = Unit()

    def test_set_location(self):
        self.unit.location = (0, 0)
        self.assertEqual(self.unit.location, (0, 0))
