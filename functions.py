import math


def is_prime(n: int) -> bool:
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def are_relatively_prime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1
