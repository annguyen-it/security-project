import math


def is_prime(n: int) -> bool:
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def are_relatively_prime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


def analysis(n: int) -> dict:
    prime_numbers = dict()
    current_division = 2
    while n > 1:
        if n % current_division == 0:
            prime_numbers[current_division] = prime_numbers[current_division] + 1 \
                if current_division in prime_numbers.keys() \
                else 1
            n /= current_division
        else:
            current_division += 1
    return prime_numbers


def test(result_test, result) -> None:
    print('result_test:', result_test)
    print('result: ', result)
    print('Ok' if result == result_test else 'Wrong result')


def find_divisor(n: int) -> [int]:
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


def hex_to_bin(hex_str: str) -> str:
    bits = "0" + str(len(hex_str) * 4) + "b"  # 08b
    return format(int(hex_str, 16), bits)


def bin_to_hex(bin_str: str) -> str:
    return hex(int(bin_str, 2))[2:]


def dec_to_bin(dec_num: int) -> str:
    bits = "04b"  # 08b
    return format(int(str(dec_num), 10), bits)


def xor(a: str, b: str) -> str:
    res = ''
    for i in range(len(a)):
        res += '0' if a[i] == b[i] else '1'
    return res


def group(arr: [], length: int):
    return [arr[n:n + length] for n in range(0, len(arr), length)]
