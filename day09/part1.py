import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Swap around free spaces (.) and files (numbers) so all free spaces lie at the end    
    file_number = 0
    line = []
    
    for i, char in enumerate(lines[0]):
        value = int(char)
        if i % 2 == 0:
            file = file_number
            file_number += 1
        else:
            file = -1
        line.extend([file] * value)


    p_space, p_file = 0, len(line) - 1
    while p_space < p_file:
        while p_space < p_file and line[p_space] != -1:
            p_space += 1

        while p_space < p_file and line[p_file] == -1:
            p_file -= 1

        if p_space < p_file:
            line[p_space], line[p_file] = line[p_file], -1

    return sum([i * n for i, n in enumerate(line[:p_space])])

INPUT_S = '''\
2333133121414131402
'''
EXPECTED = 1928


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
