from typing import List, Dict

from utils import import_input


lines: List[bytes] = import_input(3).splitlines()
symbols: Dict[int, int] = {}
for line in lines:
    for b in line:
        if b in symbols:
            symbols[b] += 1
        else:
            symbols[b] = 1
for k in dict(sorted(symbols.items())):
    print(k.to_bytes().decode("utf-8"), k, symbols[k])