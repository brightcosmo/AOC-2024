import os.path
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Evaluate whether an equation is possible given the list of numbers, being able to assign * or + between nums
    lines = [
        (int(target), [int(o) for o in operands.strip().split(" ")])
        for line in lines
        for target, operands in [line.split(":")]
    ]
    
    return sum(target for target, operands in lines if process(target, operands.copy()))

def process(target: int, operands: List[int]) -> int:
    if target < 0 or (target != 0 and not operands):
        return False
    elif target == 0 and not operands:
        return True
    
    curr_operand = operands.pop()
    quotient, remainder = divmod(target, curr_operand)
    if remainder == 0:
        if process(quotient, operands.copy()):
            return True

    return process(target - curr_operand, operands.copy())

INPUT_S = '''\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''
EXPECTED = 3749


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()