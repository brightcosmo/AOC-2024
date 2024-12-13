import os.path
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    data = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

    data = [
        sum(data[i:i+4], [])
        for i in range(0, len(data), 4)
    ]

    ans = 0
    for ax, ay, bx, by, tx, ty in data:
        a, da = divmod(tx*by-ty*bx, ax*by-ay*bx)
        b, db = divmod(ty*ax-tx*ay, ax*by-ay*bx)
        if da == db == 0:
            ans += 3*a + b
            
    return ans

INPUT_S = '''\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''
EXPECTED = 480


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
