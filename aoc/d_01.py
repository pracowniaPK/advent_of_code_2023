from typing import Dict, List
from os import path


def get_digits_dictionary() -> Dict[str, str]:
    digits_names: List[str] = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits: List[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits_combined: List[str] = []
    for name, digit in zip(digits_names, digits):
        digits_combined.append(name + digit + name)
    return dict(zip(digits_names, digits_combined))

def replace_sequences(in_string: str, replacements: Dict[str, str]) -> str:
    for old_seq, new_seq in replacements.items():
        in_string = in_string.replace(old_seq, new_seq)
    return in_string

def get_calibration_value(line: str) -> int:
    line_with_transformed_digits = replace_sequences(line, get_digits_dictionary())
    digits = [int(c) for c in line_with_transformed_digits if c.isdigit()]
    if len(digits) == 0:
        raise ValueError('Line {} does not include digits.'.format(line))
    return 10 * digits[0] + digits[-1]

if __name__ == '__main__':
    values_sum: int = 0
    input_path: str = path.join(path.dirname(__file__), 'input', '01.txt')
    with open(input_path, 'r') as f:
        for l in f:
            values_sum += get_calibration_value(l)
    print(values_sum)