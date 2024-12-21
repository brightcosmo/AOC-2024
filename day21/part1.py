import os.path
from itertools import permutations, product

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Control the robot which controls the buttons to control the keypad
    num_keys = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
    }
    
    dir_keys = {
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2)
    }

    dirs = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0)
    }
    
    def compute_ways(code, keypad):
        parts = []
        cur_loc = keypad["A"]

        for c in code:
            next_loc = keypad[c]
            di = next_loc[0] - cur_loc[0]
            dj = next_loc[1] - cur_loc[1]

            moves = ""
            if di > 0:
                moves += "v" * di
            elif di < 0:
                moves += "^" * -di
            if dj > 0:
                moves += ">" * dj
            elif dj < 0:
                moves += "<" * -dj
            
            raw_combos = list(set(["".join(x) + "A" for x in permutations(moves)]))
            combos = []
            for combo in raw_combos:
                ci, cj = cur_loc
                good = True
                for c in combo[:-1]:
                    di, dj = dirs[c]
                    ci, cj = ci + di, cj + dj
                    if not (ci, cj) in keypad.values():
                        good = False
                        break
                if good:
                    combos.append(combo)

            parts.append(combos)
            cur_loc = next_loc
        
        return ["".join(x) for x in product(*parts)]
    
    ans = 0
    for line in lines:
        ways1 = compute_ways(line, num_keys)
        ways2 = []
        for way in ways1:
            ways2.extend(compute_ways(way, dir_keys))
        ways3 = []
        for way in ways2:
            ways3.extend(compute_ways(way, dir_keys))

        ans += min([len(x) for x in ways3]) * int(line[:-1])
    
    return ans

INPUT_S = '''\
029A
980A
179A
456A
379A
'''
EXPECTED = 126384


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
