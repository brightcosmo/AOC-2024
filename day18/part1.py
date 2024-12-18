import os.path
from heapq import heappop, heappush
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Solve path for top left to bottom right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    falling_bytes = [tuple(map(int, byte.split(','))) for byte in lines]
    grid_size = max(max(map(int, line.split(','))) for line in lines) + 1
    corrupted_bytes = set(falling_bytes[:1024])

    start_position = (0, 0)
    end_position = (grid_size-1, grid_size-1)

    visited = set()
    queue = [(start_position, (1, 0), 0), (start_position, (0, 1), 0)]

    while queue:
        current_position, current_direction, steps = queue.pop(0)
        visited.add(current_position)

        if current_position==end_position:
            return steps

        x, y = current_position

        for direction in directions:
            step_x, step_y = direction
            x_n, y_n = (x + step_x), (y + step_y)

            if x_n < 0 or x_n >= grid_size or y_n < 0 or y_n >= grid_size:
                continue

            if current_direction[0] * step_x + current_direction[1] * step_y < 0:
                continue

            if (x_n, y_n) in visited:
                continue

            if (x_n, y_n) in corrupted_bytes:
                continue

            item = ((x_n, y_n), direction, steps + 1)
            if item in queue:
                continue

            queue.append(item)

INPUT_S = '''\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
'''
EXPECTED = 22


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
