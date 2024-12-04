import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # Check for X-shaped occurrence of MAS
    count = 0
    rows = len(lines)
    cols = len(lines[0])
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == "A" and i > 0 and i < rows-1 and j > 0 and j < cols-1:
                diagonal_1 = set([lines[i-1][j-1], lines[i+1][j+1]])
                diagonal_2 = set([lines[i-1][j+1], lines[i+1][j-1]])
                if {"M", "S"}.issubset(diagonal_1) and {"M", "S"}.issubset(diagonal_2):
                    count += 1

    return count


INPUT_S = '''\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
EXPECTED = 9


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
