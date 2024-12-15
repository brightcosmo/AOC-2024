import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
                
    # SOLUTION
    # Same as before with wider boxes
    grid, moves = s.split('\n\n')

    def move(p, d):
        p += d
        if all([
            grid[p] != '[' or move(p+1, d) and move(p, d),
            grid[p] != ']' or move(p-1, d) and move(p, d),
            grid[p] != '#']):
                grid[p], grid[p-d] = grid[p-d], grid[p]
                return True
    
    for grid in grid, grid.translate(str.maketrans(
            {'#':'##', '.':'..', 'O':'[]', '@':'@.'})):
        grid = {i+j*1j:c for j,r in enumerate(grid.split())
                        for i,c in enumerate(r)}
        pos, = [p for p in grid if grid[p] == '@']

        for m in moves.replace('\n', ''):
            dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
            C = grid.copy()
            if move(pos, dir): pos += dir
            else: grid = C

        ans = sum(pos for pos in grid if grid[pos] in '[')

    return int(ans.real + ans.imag*100)



INPUT_S = '''\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''
EXPECTED = 9021


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
