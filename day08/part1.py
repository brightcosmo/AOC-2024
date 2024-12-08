import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Calculate total no of affected locations, where each pair of nodes affects a tile in the same vector away from each other.

    coordinates = defaultdict(list)
    rows = len(lines)
    cols = len(lines[0])
    
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

                x1 -= dx
                y1 -= dy
                if check_bounds(x1, y1, rows, cols):
                    locations.add((x1, y1))

                x2 += dx
                y2 += dy
                if check_bounds(x2, y2, rows, cols):
                    locations.add((x2, y2))

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
EXPECTED = 14


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
