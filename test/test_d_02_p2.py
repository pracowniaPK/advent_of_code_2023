import unittest

from aoc.d_02 import Result, FewestNumbers, Game


class TestFewestNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game1 = Game([
            Result([0,2,3]),
            Result([5,1,1]),
        ])
        cls.game2 = Game([
            Result([1,2,3]),
        ])
        cls.game3 = Game([
            Result([0,2,3]),
            Result([0,10,100]),
        ])

    def test_fr_creation(self):
        fn = FewestNumbers(self.game1)
        self.assertEqual(fn.values['red'], 5)
        self.assertEqual(fn.values['green'], 2)
        self.assertEqual(fn.values['blue'], 3)
    
    def test_fr_creation_single_result(self):
        fn = FewestNumbers(self.game2)
        self.assertEqual(fn.values['red'], 1)
        self.assertEqual(fn.values['green'], 2)
        self.assertEqual(fn.values['blue'], 3)

    def test_fr_creation_zero_value(self):
        fn = FewestNumbers(self.game3)
        self.assertEqual(fn.values['red'], 0)
        self.assertEqual(fn.values['green'], 10)
        self.assertEqual(fn.values['blue'], 100)

    def test_fr_power_calculation(self):
        fn = FewestNumbers(self.game1)
        self.assertEqual(fn.calculate_power(), 30)
        
    def test_fr_power_calculation_single_result(self):
        fn = FewestNumbers(self.game2)
        self.assertEqual(fn.calculate_power(), 6)
        
    def test_fr_power_calculation_zero_value(self):
        fn = FewestNumbers(self.game3)
        self.assertEqual(fn.calculate_power(), 0)

    def test_fr_power_calculation_counting(self):
        fn1 = FewestNumbers(self.game1)
        fn2 = FewestNumbers(self.game2)
        fn3 = FewestNumbers(self.game3)
        self.assertAlmostEqual(FewestNumbers.count_powers([fn1, fn2, fn3]), 36)
        self.assertAlmostEqual(FewestNumbers.count_powers([fn1, fn2]), 36)
        self.assertAlmostEqual(FewestNumbers.count_powers([fn3]), 0)
