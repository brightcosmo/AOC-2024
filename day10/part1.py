import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Find all reachable 9's from 0 to 9 in increments of 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows, cols = len(lines), len(lines[0])
    reachable = []

    def dfs(x, y, current_value):
        if not (0 <= x < rows and 0 <= y < cols) or int(lines[x][y]) != current_value:
            return False
        if current_value == 9:
            reachable.append((x, y))
            return True
        for dx, dy in directions:
            dfs(x + dx, y + dy, current_value + 1)

    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '0':
                dfs(i, j, 0)

    return len(reachable)

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
EXPECTED = 36


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
