import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Output is supposed to be X bits + Y bits = Z bits (as a decimal number). Figure out which logic gates are wrong.
    lines = s.splitlines()
    wires = {}
    operations = []

    def process(op, op1, op2):
        if op == "AND":
            return op1 & op2
        elif op == "OR":
            return op1 | op2
        elif op == "XOR":
            return op1 ^ op2

    highest_z = "z00"
    for line in lines:
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            op1, op, op2, _, res = line.split(" ")
            operations.append((op1, op, op2, res))
            if res.startswith("z") and int(res[1:]) > int(highest_z[1:]):
                highest_z = res

    wrong = set()
    for op1, op, op2, res in operations:
        if res.startswith("z") and op != "XOR" and res != highest_z:
            wrong.add(res)
        if op == "XOR" and not any(w.startswith(("x", "y", "z")) for w in (res, op1, op2)):
            wrong.add(res)
        if op == "AND" and "x00" not in (op1, op2):
            for subop1, subop, subop2, subres in operations:
                if res in (subop1, subop2) and subop != "OR":
                    wrong.add(res)
        if op == "XOR":
            for subop1, subop, subop2, subres in operations:
                if res in (subop1, subop2) and subop == "OR":
                    wrong.add(res)

    pending_operations = operations[:]
    while pending_operations:
        op1, op, op2, res = pending_operations.pop(0)
        if op1 in wires and op2 in wires:
            wires[res] = process(op, wires[op1], wires[op2])
        else:
            pending_operations.append((op1, op, op2, res))

    return ",".join(sorted(wrong))

INPUT_S = '''\
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
'''
EXPECTED = "z00,z01,z02,z05"


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
        assert solve(f.read()) == "kcd,pfn,shj,tpk,wkb,z07,z23,z27"
    return 0


if __name__ == '__main__':
    main()
