import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Simulate 100s of robots moving on a grid, with wraparound
    width, height = map(int, lines[1].split())
    
    lines = lines[2:]
    positions = defaultdict(list)
    for line in lines:
        p, v = line.split()
        p = tuple(map(int, p.split('=')[1].split(',')))
        v = tuple(map(int, v.split('=')[1].split(',')))
        
        positions[p].append(v)
    previous_max_vertical_run = 0
    new_positions = defaultdict(list)
    for time in range(100000):
        current_positions = positions.copy()
        
        for p in current_positions:
            for v in current_positions[p]:
                x, y = p
                dx, dy = v
                new_x = (x + dx) % width
                new_y = (y + dy) % height
                new_positions[(new_x, new_y)].append(v)
        
        current_max_vertical_run = longest_vertical_run(new_positions)

        if current_max_vertical_run >= previous_max_vertical_run:
            previous_max_vertical_run = current_max_vertical_run
            print(f"Step {time + 1}: Longest vertical run = {current_max_vertical_run}")
            for y in range(height):
                row = ''.join(
                    '#' if (x, y) in new_positions else '.'
                    for x in range(width)
                )
                print(row)

        positions = new_positions
        new_positions = defaultdict(list)

    return True

def longest_vertical_run(positions):
    vertical_counts = defaultdict(int)

    for (x, y) in positions:
        vertical_counts[y] += len(positions[(x, y)])

    return max(vertical_counts.values(), default=0)

INPUT_S = '''
11 7
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''
EXPECTED = 12


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
