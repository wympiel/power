import unittest

from power import *

class PowerTest(unittest.TestCase):

    def test_power_1_1_is_1(self):
        self.assertEqual(power(1, 1), 1)

    def test_power_2_0_is_1(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_0_0_is_1(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_0_2_is_0(self):
        self.assertEqual(power(0, 2), 0)

    def negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_negative_exp(self):
        self.assertEqual(pow(2, -5), 0.03125)
    def test_fraction_exp(self):
        self.assertEqual(power(4, 0.5), 2)

if __name__ == '__main__':
    unittest.main()