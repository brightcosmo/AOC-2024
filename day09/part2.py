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
    
    for p_space, char in enumerate(lines[0]):
        value = int(char)
        if p_space % 2 == 0:
            file = file_number
            file_number += 1
        else:
            file = -1
        line.append([file, value])

    for p_file in range(len(line)-1, 0, -1):
        if line[p_file][0] == -1:
            continue
        
        file = line[p_file]
        for p_space in range(1, p_file):
            space = line[p_space]
            if space[0] != -1:
                continue
            
            elif space[1] > file[1]:
                space[1] -= file[1]
                line.insert(p_space, [file[0], file[1]])
                file[0] = -1
                break
            
            elif space[1] == file[1]:
                line[p_space], line[p_file] = line[p_file], line[p_space]
                break
                
    flattened = [x for x, y in line for _ in range(y)]
    return sum([i * n for i, n in enumerate(flattened) if n != -1])

INPUT_S = '''\
2333133121414131402
'''
EXPECTED = 2858


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
