from Chapter2.e2_extended_euclid import calc_extended_euclid
from Chapter2.e5_euler import calc_euler_modulo
from functions import test


def discrete_logarithm(a: int, b: int, x: int, y: int, n: int) -> [int]:
    ax = calc_euler_modulo(a, x, n)
    by = calc_euler_modulo(b, y, n)

    a1 = (ax + by) % n
    a2 = (ax - by) % n
    a3 = (ax * by) % n
    a4 = calc_extended_euclid(by, n)
    a5 = (a3 * a4) % n
    return [a1, a2, a3, a4, a5]


if __name__ == '__main__':
    result_test = [287, 225, 25, 17, 250]
    result = discrete_logarithm(53, 31, 336, 585, 293)
    test(result_test, result)
