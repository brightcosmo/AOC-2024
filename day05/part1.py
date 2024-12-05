import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Input a set of ordering rules, and some numbers - check which ones are following the rules, and sum the middle numbers
    separator = lines.index("")
    rules_input = lines[:separator]
    
    rules = defaultdict(list)
    i = 0
    for line in rules_input:
        nums = list(map(int, line.split("|")))
        rules[nums[0]].append(nums[1])
    
    answer = 0
    numbers = lines[separator+1:]
    for line in numbers:
        sequence = list(map(int, line.split(",")))
        
        valid = True
        for i, num in enumerate(sequence):
            if not all(num2 in rules[num] for i2, num2 in enumerate(sequence) if i2 > i): # T_T
                valid = False
                break

        answer += sequence[len(sequence)//2] * valid
    
    return answer

# TODO: change for the small example given
INPUT_S = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
EXPECTED = 143


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
