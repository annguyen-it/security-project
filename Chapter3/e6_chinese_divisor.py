from Chapter3.e1_ha_bac import calc_module
from functions import analysis, test
from Chapter3.e7_solve_set_of_equations import solve_set_of_equations


def calc_chinese_divisor(a: int, k: int, n: int) -> int:
    prime_numbers = analysis(n)
    m = []
    for num in prime_numbers:
        m.append(pow(num, prime_numbers[num]))
    # A = a^k
    # a[i] = A mod m[i]
    a = [calc_module(a, k, i) for i in m]

    return solve_set_of_equations(m, a)


if __name__ == '__main__':
    result_test = pow(191, 58) % 79663
    result = calc_chinese_divisor(191, 58, 79663)
    test(result_test, result)
