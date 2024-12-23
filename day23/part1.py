import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Find sets of 3 connected graphs, and return all that has at least 1 graph starting with t
    graph = defaultdict(set)
    for line in lines:
        node1, node2 = line.strip().split('-')
        graph[node1].add(node2)
        graph[node2].add(node1)
    
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 < neighbor2 and neighbor2 in graph[neighbor1]:
                    triangles.add(tuple(sorted([node, neighbor1, neighbor2])))

    return len([triangle for triangle in triangles if any(node.startswith('t') for node in triangle)])

INPUT_S = '''\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''
EXPECTED = 7


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
