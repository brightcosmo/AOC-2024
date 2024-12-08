import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Same total as before, but now include all antinodes in a line (spaced apart by distance, and including on the original nodes)

    coordinates = defaultdict(list)
    rows, cols = len(lines), len(lines[0])
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char != ".":
                coordinates[char].append((i, j))
    
    locations = set()
    for nodes in coordinates.values():
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]
                dx, dy = calculate_vector(x1, y1, x2, y2)

                for x, y, step in [(x1, y1, -1), (x2, y2, 1)]:
                    while check_bounds(x, y, rows, cols):
                        locations.add((x, y))
                        x += step * dx
                        y += step * dy

    return len(locations)

def check_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def calculate_vector(x1, y1, x2, y2):
    return (x2 - x1, y2 - y1)


INPUT_S = '''\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''
EXPECTED = 34


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
