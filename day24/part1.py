import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Evaluate the logic gates in the correct order.
    lines = s.strip().split("\n")
    values = {}
    split_index = lines.index("")
    
    for line in lines[:split_index]:
        key, value = line.split(":")
        values[key.strip()] = int(value.strip())
    
    pending_instructions = lines[split_index + 1:]
    while pending_instructions:
        next_round = []
        for instruction in pending_instructions:
            parts = instruction.split(" -> ")
            operation = parts[0]
            result = parts[1].strip()

            try:
                if "AND" in operation:
                    operands = operation.split(" AND ")
                    values[result] = values[operands[0].strip()] & values[operands[1].strip()]
                elif "XOR" in operation:
                    operands = operation.split(" XOR ")
                    values[result] = values[operands[0].strip()] ^ values[operands[1].strip()]
                elif "OR" in operation:
                    operands = operation.split(" OR ")
                    values[result] = values[operands[0].strip()] | values[operands[1].strip()]
            except KeyError:
                next_round.append(instruction)
        pending_instructions = next_round

    binary_representation = "".join(str(values[key]) for key in sorted(values, reverse=True) if key.startswith('z'))
    return int(binary_representation, 2)

INPUT_S = '''\
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
'''
EXPECTED = 4


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
