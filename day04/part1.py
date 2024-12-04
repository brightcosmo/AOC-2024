import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)

    # SOLUTION
    # Check for all occurrences of "XMAS", including horizontal, vertical, diagonal, backwards
    count = 0
    rows = len(lines)
    cols = len(lines[0])
    
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == "X":
                can_go_down = i+3 < rows
                can_go_up = i-3 >= 0
                can_go_right = j+3 < cols
                can_go_left = j-3 >= 0

                # Check vertical
                if can_go_down:
                    if f"{lines[i+1][j]}{lines[i+2][j]}{lines[i+3][j]}" == "MAS":
                        count += 1

                # Check vertical backwards
                if can_go_up:
                    if f"{lines[i-1][j]}{lines[i-2][j]}{lines[i-3][j]}" == "MAS":
                        count += 1

                # Check horizontal
                if can_go_right:
                    if f"{lines[i][j+1]}{lines[i][j+2]}{lines[i][j+3]}" == "MAS":
                        count += 1

                # Check horizontal backwards
                if can_go_left:
                    if f"{lines[i][j-1]}{lines[i][j-2]}{lines[i][j-3]}" == "MAS":
                        count += 1

                # Check diagonal (bottom-left)
                if can_go_down and can_go_left:
                    if f"{lines[i+1][j-1]}{lines[i+2][j-2]}{lines[i+3][j-3]}" == "MAS":
                        count += 1

                # Check diagonal (bottom-right)
                if can_go_down and can_go_right:
                    if f"{lines[i+1][j+1]}{lines[i+2][j+2]}{lines[i+3][j+3]}" == "MAS":
                        count += 1

                # Check diagonal (top-left)
                if can_go_up and can_go_left:
                    if f"{lines[i-1][j-1]}{lines[i-2][j-2]}{lines[i-3][j-3]}" == "MAS":
                        count += 1

                # Check diagonal (top-right)
                if can_go_up and can_go_right:
                    if f"{lines[i-1][j+1]}{lines[i-2][j+2]}{lines[i-3][j+3]}" == "MAS":
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
EXPECTED = 18


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
