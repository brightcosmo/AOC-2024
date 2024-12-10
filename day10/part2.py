import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Find all valid paths from 0 to 9 in increments of 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    grid = [[int(cell) for cell in line] for line in lines]
    starting_points = [(i, j) for i, row in enumerate(lines) for j, cell in enumerate(row) if cell == '0']
    valid_paths = []
    rows = len(grid)
    cols = len(grid[0])
    
    def dfs(path, x, y, current_value):
        if current_value == 9:
            valid_paths.append(path[:])
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == current_value + 1:
                dfs(path + [(nx, ny)], nx, ny, current_value + 1)
    
    for s in starting_points:
        dfs([s], s[0], s[1], 0)
        
    return len(valid_paths)

INPUT_S = '''\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''
EXPECTED = 81


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
