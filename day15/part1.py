import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
                
    # SOLUTION
    # Move robot in certain directions, pushing boxes and resisting walls
    grid_end = lines.index('')
    robotFound = False
    robot = None
    grid = []
    for r, line in enumerate(lines[:grid_end]):
        row = list(line)
        grid.append(row)
        if not robotFound:
            for c, char in enumerate(row):
                if char == '@':
                    robot = (r, c)
                    robotFound = True
                    break
    
    directions = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }    
    arrows = [char for line in lines[grid_end + 1:] for char in line.strip()]
    arrows = [directions[arrow] for arrow in arrows]

    def push(grid, box, dirs) -> bool:
        in_front = grid[box[0] + dirs[0]][box[1] + dirs[1]]
        if in_front == ".":
            grid[box[0]][box[1]] = "."
            grid[box[0]+dirs[0]][box[1]+dirs[1]] = "O"
            return True
        elif in_front == "#":
            return False
        elif in_front == "O":
            if push(grid, (box[0] + dirs[0], box[1] + dirs[1]), dirs):
                grid[box[0]][box[1]] = "."
                grid[box[0]+dirs[0]][box[1]+dirs[1]] = "O"
                return True
            else:
                return False
            
    for move in arrows:
        in_front = grid[robot[0] + move[0]][robot[1] + move[1]] 
        if in_front == ".":
            new_robot = (robot[0] + move[0], robot[1] + move[1])
            grid[new_robot[0]][new_robot[1]] = "@"
            grid[robot[0]][robot[1]] = "."
            robot = new_robot
        elif in_front == "O":
            if push(grid, (robot[0] + move[0], robot[1] + move[1]), move):
                new_robot = (robot[0] + move[0], robot[1] + move[1])
                grid[new_robot[0]][new_robot[1]] = "@"
                grid[robot[0]][robot[1]] = "."
                robot = new_robot
        
    box_sum = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                box_sum += 100 * y + x
    
    return box_sum



INPUT_S = '''\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''
EXPECTED = 2028


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
