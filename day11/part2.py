import os.path
from collections import Counter, defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Same as part 1, but with 75 iterations (need memo for realistic computation time)
    stones = list(map(int, lines[0].split()))
    stones = Counter(stones)

    for _ in range(75):
        new_stones = defaultdict(int)
        
        for stone in stones:
            digits = str(stone)
            length = len(digits)
            num = stones[stone]
            
            if stone == 0:
                new_stones[1] += num
            elif length % 2 == 0:
                mid = length // 2
                new_stones[int(digits[:mid])] += num
                new_stones[int(digits[mid:])] += num
            else:
                new_stones[stone * 2024] += num
        stones = new_stones

    return sum(stones.values())

INPUT_S = '''\
125 17
'''
EXPECTED = 65601038650482


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    test()
