import os.path
from bisect import bisect
import networkx as nx
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Find the coordinate that makes a path impossible
    data = [tuple(map(int, byte.split(','))) for byte in lines]
    grid_size = max(max(map(int, line.split(','))) for line in lines) + 1
    graph = nx.grid_2d_graph(grid_size, grid_size)
    grid_size -= 1
    
    for i, p in enumerate(data):
        graph.remove_node(p)
        if not nx.has_path(graph, (0, 0), (grid_size, grid_size)):
            return p

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
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
'''
EXPECTED = (6, 1)


def test() -> None:
    print(solve(INPUT_S))
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
