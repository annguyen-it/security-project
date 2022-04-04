from typing import Optional


# a^-1 mod n
def calc_extended_euclid(a: int, n: int) -> Optional[int]:
    a2, a3 = 0, n
    b2, b3 = 1, a

    while b3 not in [0, 1]:
        q = a3 // b3
        new_a2, new_a3 = b2, b3
        b2 = a2 - q * b2
        b3 = a3 - q * b3
        a2, a3 = new_a2, new_a3

    if b3 == 0:
        return None

    return b2 % n


if __name__ == '__main__':
    res = calc_extended_euclid(3331, 6551)
    print(res)
