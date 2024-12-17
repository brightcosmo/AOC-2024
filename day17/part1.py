import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # 3 bit CPU with 7 operands
    registers = {}
    program_numbers = []
    for line in lines[:3]:
        reg_name, reg_value = line.split(': ')
        registers[reg_name.split(' ')[1]] = int(reg_value)

    a = registers['A']
    b = registers['B']
    c = registers['C']

    program_line = lines[4].split(': ')[1]
    program_numbers = list(map(int, program_line.split(',')))
    
    output = []
    i = 0
    def decode(a, b, c, val):
        return [0, 1, 2, 3, a, b, c][val]
    
    while i < len(program_numbers):
        opcode = program_numbers[i]
        operand = program_numbers[i+1]

        if opcode == 0:
            a = int(a / (2 ** decode(a, b, c, operand)))
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = decode(a, b, c, operand) % 8
        elif opcode == 3:
            if a != 0:
                i = operand
                i -= 2
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(decode(a, b, c, operand) % 8)
        elif opcode == 6:
            b = int(a / (2 ** decode(a, b, c, operand)))
        elif opcode == 7:
            c = int(a / (2 ** decode(a, b, c, operand)))
        i += 2
    print(",".join(map(str, output)))
    return ",".join(map(str, output))


INPUT_S = '''\
Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
'''
EXPECTED = "4,6,3,5,6,3,5,2,1,0"


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    test()
