from typing import Dict, List
from re import search

class Result:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = r
        self.g = g
        self.b = b

def get_game_results(line: str) -> List[Result]:
    line = line.split(': ')[1]
    results_list_raw: List[str] = line.split(';')
    results_list: List[Result] =[]
    for str_result in results_list_raw:
        print(search(r'\d\b', str_result))

def load_games(file_path):
    with open(file_path) as f:
        for line in f:
            pass


load_games('AdventOfCode\\2023\\input\\02.txt')
get_game_results('Game 17: 2 blue, 4 green, 3 red; 2 red, 5 green, 11 blue; 5 green, 15 blue, 2 red; 3 green, 13 blue; 6 blue, 2 green, 2 red; 8 blue, 1 red')