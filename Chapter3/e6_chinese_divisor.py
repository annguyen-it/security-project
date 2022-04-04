from functions import analysis, test
from Chapter3.e7_solve_set_of_equations import solve_set_of_equations


def calc_chinese_divisor(a: int, k: int, n: int) -> int:
    A = pow(a, k)

    prime_numbers = analysis(n)
    m = []
    for key in prime_numbers:
        m.append(pow(key, prime_numbers[key]))
    a = [A % i for i in m]

    return solve_set_of_equations(m, a)


if __name__ == '__main__':
    result_test = pow(191, 58) % 79663
    result = calc_chinese_divisor(191, 58, 79663)
    test(result_test, result)
