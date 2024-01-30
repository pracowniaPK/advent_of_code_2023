import unittest
from sys import path

from aoc.d_01 import get_calibration_value, replace_sequences
from aoc.d_02 import Result, Game


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

class TestDay02(unittest.TestCase):
    def test_result_creation_from_srt(self):
        result = Result.result_from_str('2 blue, 14 green, 3 red')
        self.assertEqual(result.values['red'], 3)
        self.assertEqual(result.values['green'], 14)
        self.assertEqual(result.values['blue'], 2)

        result = Result.result_from_str('1 green, 3 red, 6 blue')
        self.assertEqual(result.values['red'], 3)
        self.assertEqual(result.values['green'], 1)
        self.assertEqual(result.values['blue'], 6)

    def test_result_creation_from_srt_not_all_values_set(self):
        result1 = Result.result_from_str('20 blue, 1 green')
        self.assertEqual(result1.values['red'], 0)
        self.assertEqual(result1.values['green'], 1)
        self.assertEqual(result1.values['blue'], 20)
        
        result2 = Result.result_from_str('3 red, 12 blue')
        self.assertEqual(result2.values['red'], 3)
        self.assertEqual(result2.values['green'], 0)
        self.assertEqual(result2.values['blue'], 12)
        
        result3 = Result.result_from_str('3 green, 6 red')
        self.assertEqual(result3.values['red'], 6)
        self.assertEqual(result3.values['green'], 3)
        self.assertEqual(result3.values['blue'], 0)
        
    def test_result_creation_from_empty_srt(self):
        result = Result.result_from_str('')
        self.assertEqual(result.values['red'], 0)
        self.assertEqual(result.values['green'], 0)
        self.assertEqual(result.values['blue'], 0)

    def test_result_to_string(self):
        result = Result([0, 8, 16])
        self.assertEqual(str(result), 'Result: 0 red, 8 green, 16 blue')

    def test_result_repr(self):
        result = Result([0, 8, 16])
        self.assertEqual(repr(result), '<Result: 0 red, 8 green, 16 blue>')

    def test_result_validation(self):
        thresholds = {'red': 3, 'green': 4, 'blue': 5}
        result1 = Result([2, 3, 4])
        self.assertTrue(result1.is_valid(thresholds))
        result2 = Result([4, 3, 2])
        self.assertFalse(result2.is_valid(thresholds))

    def test_game_counting_valid(self):
        thresholds = {'red': 3, 'green': 4, 'blue': 14}
        games_list = [
            Game([Result([3,4,5]), Result([1,2,3]), Result([1,2,13])]),
            Game([Result([11,2,3]), Result([1,2,3]), Result([1,2,3])]),
            Game([Result([1,2,3])])
        ]
        self.assertEqual(Game.count_valid_games(games_list, thresholds), 4)

    def test_getting_results_from_line(self):
        line = 'Game 13: 7 blue, 8 red; 5 green, 15 blue, 2 red; 7 green, 3 blue, 12 red'
        game = Game.game_from_str(line)
        self.assertEqual(game.results[1].values['red'], 2)
        self.assertEqual(game.results[1].values['green'], 5)
        self.assertEqual(game.results[1].values['blue'], 15)
        

class TestUtils(unittest.TestCase):
    def test_sequensces_replacing(self):
        replacements = {
            'one': '1',
            'two': '2',
        }
        self.assertEqual(replace_sequences('one1two2twooo', replacements), '11222oo')

if __name__ == '__main__':
    unittest.main()
