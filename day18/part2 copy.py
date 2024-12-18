import os.path
from bisect import bisect
import networkx as nx
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Solve path for top left to bottom right
    data = [tuple(map(int, byte.split(','))) for byte in lines]
    G = nx.grid_2d_graph(71, 71)

    for i, p in enumerate(data):
        G.remove_node(p)
        if i == 1023:
            # Part 1
            print(nx.shortest_path_length(G, (0, 0), (70, 70)))
        elif not nx.has_path(G, (0, 0), (70, 70)):
            # Part 2
            print(p)
            break

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
