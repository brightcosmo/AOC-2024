import os.path
from collections import defaultdict
from heapq import heappop, heappush
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Solve path for S to E in maze, and get all best paths
    grid = {i+j*1j: c for i,r in enumerate(lines)
                    for j,c in enumerate(r) if c != '#'}

    start, = (p for p in grid if grid[p] == 'S')

    seen = []
    best = 1e9
    dist = defaultdict(lambda: 1e9)
    stack = [(0, t:=0, start, 1j, [start])]

    while stack:
        val, _, pos, dir, path = heappop(stack)

        if val > dist[pos, dir]: continue
        else: dist[pos, dir] = val

        if grid[pos] == 'E' and val <= best:
            seen += path
            best = val

        for r, v in (1, 1), (+1j, 1001), (-1j, 1001):
            v, t, p, d = val+v, t+1, pos + dir*r, dir*r
            if p not in grid: continue
            heappush(stack, (v, t, p, d, path + [p]))


    return len(set(seen))
    
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
EXPECTED = 45


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
