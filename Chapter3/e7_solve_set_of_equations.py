from Chapter3.e2_extended_euclid import calc_extended_euclid
from functions import test


def solve_set_of_equations(m: [int], a: [int]) -> [int]:
    n = 1
    for i in m:
        n *= i

    # M[i] = n / m[i]
    M = [n // i for i in m]
    c = []
    for i in range(len(m)):
        c.append(M[i] * calc_extended_euclid(M[i], m[i]))

    res = 0
    for i in range(len(m)):
        res += a[i] * c[i]
    res %= n
    return res


if __name__ == '__main__':
    result_test = 502
    result = solve_set_of_equations([19, 11, 13], [8, 2, 8])
    test(result_test, result)
