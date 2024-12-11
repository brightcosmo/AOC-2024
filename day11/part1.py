import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Apply 3 rules to the stones, and return the final number after 25 iterations
        # If 0, it becomes 1
        # If even number of digits, split evenly into 2 stones
        # Else, multiply by 2024
    stones = list(map(int, lines[0].split()))
    for _ in range(75):
        new_stones = []
        for stone in stones:
            digits = str(stone)
            length = len(digits)
            if stone == 0:
                new_stones.append(1)
            elif length % 2 == 0:
                mid = length // 2
                new_stones.extend([int(digits[:mid]), int(digits[mid:])])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)

INPUT_S = '''\
125 17
'''
EXPECTED = 55312


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()