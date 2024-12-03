import os.path
import re
from typing import Tuple

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Sum the product of all numbers which occur as the pattern mul(x, y)
    # Ignore instructions after "don't()" and start reading again after "do()"
        # Approach: Replace  "don't()....do()" and "don't()...." with empty text
    s = re.sub(r"don't\(\)(?:.*?do\(\)|.*$)", "", s, flags=re.M | re.S)  
    matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    return sum([int(x) * int(y) for x, y in matches])

INPUT_S = '''\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''
EXPECTED = 48


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
