import os.path
from collections import Counter

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Calculate the similarity score (defined as currentNumInList1 * noOccurrencesInList2) over all numbers
    nums = [tuple(map(int, line.strip().split())) for line in lines]
    left, right = tuple(zip(*nums))
    counts = Counter(right)
    answer = sum(n * counts[n] for n in left)
    return answer

INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 31


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
