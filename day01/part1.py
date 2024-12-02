import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Calculate the total sum of differences between the smallest number, second smallest... until largest
    nums = [tuple(map(int, line.strip().split())) for line in lines]
    left, right = tuple(zip(*nums))
    answer = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
    return answer

INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 11


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
