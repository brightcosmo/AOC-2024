import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Multiply the perimeter of a region by its area
    grid = defaultdict(lambda:'!')
    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line):
            grid[row_idx + 1j * col_idx] = char
    
    price = 0
    unvisited = set(grid.keys())

    while unvisited:
        start = unvisited.pop()
        region_char = grid[start]
        stack = [start]
        area = 0
        perimeter = 0
        edges = set()

        while stack:
            node = stack.pop()
            area += 1
            perimeter += 4

            for direction in (1, -1, 1j, -1j):
                neighbor = node + direction

                if grid[neighbor] != region_char:
                    edges.add((node, direction))
                    continue
                perimeter -= 1

                if neighbor not in unvisited:
                    continue

                unvisited.remove(neighbor)
                stack.append(neighbor)
        
        price += area * perimeter

    return price


INPUT_S = '''\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''
EXPECTED = 1930


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
