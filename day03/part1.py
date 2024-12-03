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
    matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    return sum([int(x) * int(y) for x, y in matches])

INPUT_S = '''\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''
EXPECTED = 161


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
