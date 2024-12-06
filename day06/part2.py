import os.path
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Find all positions resulting in infinite loop
    matrix = [list(line) for line in lines]
    
    for y, line in enumerate(matrix):
        if '^' in line:
            origin = (line.index('^'), y)
            break
    
    bottom_border = len(matrix) - 1
    right_border = len(matrix[0]) - 1
    
    def trace_path(current_matrix: List[List[int]]) -> bool:
        x, y = origin
        direction = 0
        direction_locations = set()
        
        while True:
            match direction:
                case 0:  # up
                    if y == 0:
                        return False
                    if current_matrix[y-1][x] == "#":
                        direction = 1
                    else:
                        y -= 1
                        if (x, y, direction) in direction_locations:
                            return True
                        direction_locations.add((x, y, direction))
                
                case 1:  # right
                    if x == right_border:
                        return False
                    if current_matrix[y][x+1] == "#":
                        direction = 2
                    else:
                        x += 1
                        if (x, y, direction) in direction_locations:
                            return True
                        direction_locations.add((x, y, direction))

                case 2:  # down
                    if y == bottom_border:
                        return False
                    if current_matrix[y+1][x] == "#":
                        direction = 3
                    else:
                        y += 1
                        if (x, y, direction) in direction_locations:
                            return True
                        direction_locations.add((x, y, direction))

                case 3:  # left
                    if x == 0:
                        return False
                    if current_matrix[y][x-1] == "#":
                        direction = 0
                    else:
                        x -= 1
                        if (x, y, direction) in direction_locations:
                            return True
                        direction_locations.add((x, y, direction))
    
    locations = set()
    x, y = origin
    direction = 0
    
    while True:
        match direction:
            case 0:
                if y == 0:
                    break
                if matrix[y-1][x] == "#":
                    direction = 1
                else:
                    y -= 1
                    locations.add((x, y))
            
            case 1: 
                if x == right_border:
                    break
                if matrix[y][x+1] == "#":
                    direction = 2
                else:
                    x += 1
                    locations.add((x, y))

            case 2: 
                if y == bottom_border:
                    break
                if matrix[y+1][x] == "#":
                    direction = 3
                else:
                    y += 1
                    locations.add((x, y))

            case 3: 
                if x == 0:
                    break
                if matrix[y][x-1] == "#":
                    direction = 0
                else:
                    x -= 1
                    locations.add((x, y))
    
    obstacles = 0
    for i, j in locations:
        current = [row[:] for row in matrix]
        current[j][i] = "#"
        if trace_path(current):
            obstacles += 1
    
    return obstacles

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
EXPECTED = 6


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
