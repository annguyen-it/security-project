from typing import Optional

from functions import test


# dlog(a) b mod n = x khi a^x mod n = b mod n
def discrete_logarithm(a: int, b: int, n: int) -> Optional[int]:
    for i in range(n):
        if pow(a, i) % n == b % n:
            return i
    return None


if __name__ == '__main__':
    result_test = None
    result = discrete_logarithm(3, 4, 13)
    test(result_test, result)
