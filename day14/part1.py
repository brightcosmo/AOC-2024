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
    
    new_positions = defaultdict(list)
    for _ in range(100):
        current_positions = positions.copy()
        
        for p in current_positions:
            for v in current_positions[p]:
                x, y = p
                dx, dy = v
                new_x = (x + dx) % width
                new_y = (y + dy) % height
                new_positions[(new_x, new_y)].append(v)
        
        positions = new_positions
        new_positions = defaultdict(list)
    
    mid_x, mid_y = width // 2, height // 2
    quadrants = {
        'Q1': 0,
        'Q2': 0,
        'Q3': 0,
        'Q4': 0 
    }
    
    for (x, y), robots in positions.items():
        if x == mid_x or y == mid_y:
            continue
        
        if x > mid_x and y > mid_y:
            quadrants['Q1'] += len(robots)
        elif x < mid_x and y > mid_y:
            quadrants['Q2'] += len(robots)
        elif x < mid_x and y < mid_y:
            quadrants['Q3'] += len(robots)
        elif x > mid_x and y < mid_y:
            quadrants['Q4'] += len(robots)

    return quadrants['Q1'] * quadrants['Q2'] * quadrants['Q3'] * quadrants['Q4']


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
