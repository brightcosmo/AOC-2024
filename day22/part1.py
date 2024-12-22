import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    for line in lines:
        print(line)
    
    # SOLUTION
    # Calculate secret number using operations
    secrets = [int(num) for num in lines]
    
    def prune(number):
        return number % 16777216

    def mix(secret, value):
        return secret ^ value
    
    ans = 0
    for num in secrets:
        for _ in range(2000):
            step1 = num * 64
            num = mix(num, step1)
            num = prune(num)

            step2 = num // 32
            num = mix(num, step2)
            num = prune(num)

            step3 = num * 2048
            num = mix(num, step3)
            num = prune(num)
        
        ans += num
        print(num)
    
    print(ans)
    return ans

INPUT_S = '''\
1
10
100
2024
'''
EXPECTED = 37327623


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
