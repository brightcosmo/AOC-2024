import os.path
from itertools import combinations

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Count all possible "cheats" in the path - where 100 tiles saved from spending up to 2 seconds going through walls
    grid = {i+j*1j: c for i,r in enumerate(lines)
                    for j,c in enumerate(r) if c != '#'}
    start, = (p for p in grid if grid[p] == 'S')


    dist = {start: 0}
    todo = [start]

    for pos in todo:
        for new in pos-1, pos+1, pos-1j, pos+1j:
            if new in grid and new not in dist:
                dist[new] = dist[pos] + 1
                todo += [new]


    a = 0

    for (p,i), (q,j) in combinations(dist.items(), 2):
        d = abs((p-q).real) + abs((p-q).imag)
        if d == 2 and j-i-d >= 100: a += 1
        if d < 21 and j-i-d >= 100: b += 1

    return a

INPUT_S = '''\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''
EXPECTED = 0


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
