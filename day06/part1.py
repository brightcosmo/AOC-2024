import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Traverse through the grid, starting from ^, turning 90 degrees at an obstacle, until it leaves
    matrix = [list(line) for line in lines]
    
    for y, line in enumerate(matrix):
        if '^' in line:
            x = line.index('^')
            break
    
    bottom_border = len(matrix) - 1
    right_border = len(matrix[0]) - 1
    
    direction = 0
    locations = set()

    while True:
        match direction:
            case 0:  # up
                if y == 0:
                    break
                if matrix[y-1][x] == "#":
                    direction = 1
                else:
                    y -= 1
                    locations.add((x, y))
            
            case 1:  # right
                if x == right_border:
                    break
                if matrix[y][x+1] == "#":
                    direction = 2
                else:
                    x += 1
                    locations.add((x, y))

            case 2:  # down
                if y == bottom_border:
                    break
                if matrix[y+1][x] == "#":
                    direction = 3
                else:
                    y += 1
                    locations.add((x, y))

            case 3:  # left
                if x == 0:
                    break
                if matrix[y][x-1] == "#":
                    direction = 0
                else:
                    x -= 1
                    locations.add((x, y))
    
    return len(locations)

INPUT_S = '''\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
EXPECTED = 41


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
