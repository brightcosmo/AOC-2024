import os.path
import functools

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Count all possible towels; towels can only consist of the designs from the first line
    towels = set(lines[0].strip().split(', '))
    
    @functools.cache
    def find_patterns(design):

        if len(design) == 0:
            return 1
        if len(towels) == 0:
            return 0
        count = 0
        for towel in towels:
            if design.startswith(towel):
                count += find_patterns(design[len(towel):])
        return count
    
    count = 0
    for design in lines[2:]:
        if find_patterns(design.strip()):
            count += 1
    
    return count

INPUT_S = '''\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''
EXPECTED = 6


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
