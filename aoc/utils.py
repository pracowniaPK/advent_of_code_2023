from typing import Dict


def replace_sequences(in_string: str, replacements: Dict[str, str]) -> str:
    for old_seq, new_seq in replacements.items():
        in_string = in_string.replace(old_seq, new_seq)
    return in_string

