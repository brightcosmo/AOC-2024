import os.path
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Determine if rows are safe, with a tolerance of one removed number from the sequence.
    sequences = (list(map(int, line.split())) for line in lines)
    return sum([check_safety(seq) for seq in sequences])

def check_safety(seq: List[int]) -> bool:
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return (max(diffs) <= 3 and min(diffs) >= 1) or (max(diffs) <= -1 and min(diffs) >= -3)

INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
