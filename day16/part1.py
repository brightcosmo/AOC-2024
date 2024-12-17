import os.path
from heapq import heappop, heappush
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Solve path for S to E in maze
    
    maze = lines
    
    DIRECTIONS = {
        'E': (0, 1), 
        'S': (1, 0),
        'W': (0, -1),
        'N': (-1, 0),
    }
    DIR_ORDER = ['E', 'S', 'W', 'N']
    start, end = None, None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    
    def heuristic(pos, end):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    pq = []
    heappush(pq, (0, start, 'E', 0))
    visited = set()

    while pq:
        score, (x, y), direction, steps = heappop(pq)

        if (x, y) == end:
            return score

        if ((x, y), direction) in visited:
            continue
        visited.add(((x, y), direction))

        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            heappush(pq, (score + 1, (nx, ny), direction, steps + 1))

        current_dir_idx = DIR_ORDER.index(direction)
        for turn_cost, new_dir_idx in [(1000, (current_dir_idx + 1) % 4), (1000, (current_dir_idx - 1) % 4)]:
            new_direction = DIR_ORDER[new_dir_idx]
            heappush(pq, (score + turn_cost, (x, y), new_direction, steps))

    return float('inf')

INPUT_S = '''\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''
EXPECTED = 7036


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
