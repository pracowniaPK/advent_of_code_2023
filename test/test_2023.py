import unittest
from sys import path

from aoc.d_01 import get_calibration_value
from aoc.utils import replace_sequences


class TestDay01(unittest.TestCase):
    def test_line_with_two_digits(self):
        self.assertEqual(get_calibration_value('zwo3eht4fou'), 34)

    def test_line_with_written_digits(self):
        self.assertEqual(get_calibration_value('one3ehttwo4fou'), 14)
        self.assertEqual(get_calibration_value('raefd3ehttwo45four'), 34)
        self.assertEqual(get_calibration_value('eightwothree'), 83)
        self.assertEqual(get_calibration_value('xtwone3four'), 24)

    def test_long_line(self):
        self.assertEqual(get_calibration_value(
            'jjhxddmg5mqxqbgfivextlcpnvtwothreetwonerzkjqlfcmpd4foureightfivenine5ninetsfhmclvcb8dsixhfbnlvhd76kmxf414pm9hgjzb9kpd')
            , 59)

    def test_line_with_one_digit(self):
        self.assertEqual(get_calibration_value('zwo7fou'), 77)

    def test_line_with_zero_digits(self):
        with self.assertRaises(ValueError):
            get_calibration_value('zwoehtfou')

    def test_empty_line(self):
        with self.assertRaises(ValueError):
            get_calibration_value('')

class TestUtils(unittest.TestCase):
    def test_sequensces_replacing(self):
        replacements = {
            'one': '1',
            'two': '2',
        }
        self.assertEqual(replace_sequences('one1two2twooo', replacements), '11222oo')

if __name__ == '__main__':
    unittest.main()
