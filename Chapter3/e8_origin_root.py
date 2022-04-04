from Chapter3.e4_euler_function import calc_fi
from functions import test, are_relatively_prime, find_divisor


# a là căn nguyên thủy của n
def calc_origin_root(a: int, n: int) -> bool:
    if not are_relatively_prime(a, n):
        return False

    fi_n = calc_fi(n)
    divisors = find_divisor(fi_n)
    for d in divisors:
        if pow(a, d) % n == 1 and d < fi_n:
            return False
    return True


if __name__ == '__main__':
    result_test = True
    result = calc_origin_root(3, 353)
    test(result_test, result)
