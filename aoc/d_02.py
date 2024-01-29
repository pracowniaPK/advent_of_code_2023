from __future__ import annotations
from typing import List, Dict
from re import search, Match
from os import path


class Result:
    COLORS: List[str] = ['red', 'green', 'blue']

    def __init__(self, values: List[int]):
        self.values: Dict[str, int] = {
            color: value for color, value in zip(self.COLORS, values)
            }

    def __str__(self) -> str:
        representation: str = "Result: "
        for color in self.COLORS:
            representation += "{} {}".format(self.values[color], color)
            if color != self.COLORS[-1]:
                representation += ", "
        return representation
    
    def __repr__(self) -> str:
        return "<" + self.__str__() + ">"
    
    def is_valid(self, thresholds: Dict[str, int]) -> bool:
        for color in thresholds:
            if self.values[color] > thresholds[color]:
                return False
        return True
    
    @staticmethod
    def _get_color_number(color, params_str: str) -> int:
        pattern: str = r'(\d+)\s' + color
        match: Match | None = search(pattern, params_str)
        if match:
            return int(match.group(1))
        else:
            return 0

    @classmethod
    def result_from_str(cls, params_str: str) -> cls:
        arguments: List[int] = [
            cls._get_color_number(color, params_str) for color in cls.COLORS
            ]
        return cls(arguments)

class FewestNumbers(Result):
    def __init__(self, game: Game):
        fewest_values: List[int] = []
        for color in self.COLORS:
            max_value: int = 0
            for result in game.results:
                max_value = max(max_value, result.values[color])
            fewest_values.append(max_value)
        super().__init__(fewest_values)
        
    def calculate_power(self) -> int:
        power: int = 1
        for color in self.COLORS:
            power *= self.values[color]
        return power

    @staticmethod
    def count_powers(fewest_numbers_list: List[FewestNumbers]) -> int:
        power_sum: int = 0
        for fn in fewest_numbers_list:
            power_sum += fn.calculate_power()
        return power_sum

class Game:
    def __init__(self, results: List[Result]):
        self.results = results

    def __repr__(self) -> str:
        representation: str = "Game: "
        for result in self.results:
            representation += repr(result)
            if result != self.results[-1]:
                representation += ", "
        return representation
    
    def is_valid(self, thresholds: Dict[str, int]) -> bool:
        for result in self.results:
            if not result.is_valid(thresholds):
                return False
        return True

    @classmethod
    def game_from_str(cls, line: str) -> cls:
        line = line.split(': ')[1]
        results_list_str: List[str] = line.split(';')
        results_list: List[Result] = [
            Result.result_from_str(res_str) for res_str in results_list_str
            ]
        return cls(results_list)

    @staticmethod
    def load_games(file_path) -> List[Game]:
        games_list: List[Game] = []
        with open(file_path) as f:
            for line in f:
                games_list.append(Game.game_from_str(line))
        return games_list
    
    @staticmethod
    def count_valid_games(games: List[Game], thresholds: Dict[str, int]) -> int:
        valid_ids_sum: int = 0
        for i in range(len(games)):
            if games[i].is_valid(thresholds):
                valid_ids_sum += i+1
        return valid_ids_sum

if __name__ == '__main__':
    thresholds: Dict[str, int] = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    input_path: str = path.join(path.dirname(__file__), 'input', '02.txt')
    games: List[Game] = Game.load_games(input_path)
    print('Part one solution:', Game.count_valid_games(games, thresholds))

    fewest_numbers_list: List[FewestNumbers] = []
    for game in games:
        fewest_numbers_list.append(FewestNumbers(game))
    print('Part two solution:', FewestNumbers.count_powers(fewest_numbers_list))
