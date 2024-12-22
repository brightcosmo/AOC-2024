import os.path
from collections import defaultdict
from functools import reduce
from itertools import accumulate, pairwise
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Calculate previous 4 steps from every max number
    secrets = [int(num) for num in lines]
    
    def prune(number):
        return number % 16777216

    def mix(secret, value):
        return secret ^ value
    
    def evolve(num):
        step1 = num * 64
        num = mix(num, step1)
        num = prune(num)

        step2 = num // 32
        num = mix(num, step2)
        num = prune(num)

        step3 = num * 2048
        num = mix(num, step3)
        num = prune(num)
        return num
    

    bananas = defaultdict(int)
    for num in secrets:
        steps = list(accumulate(range(2000), lambda acc, _: evolve(acc), initial=num))
        delta = [y % 10 - x % 10 for x, y in pairwise(steps)]
        seen = set()
        for i in range(len(steps) - 4):
            cur = tuple(delta[i : i + 4])
            if cur in seen:
                continue
            seen.add(cur)
            bananas[cur] += steps[i + 4] % 10
    return max(bananas.values())

INPUT_S = '''\
1
10
100
2024
'''
EXPECTED = 23


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
