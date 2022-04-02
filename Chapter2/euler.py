from functions import are_relatively_prime
from euler_function import calc_fi
from Chapter2.ha_bac import calc_module


def calc_euler_module(a: int, m: int, n: int) -> int:
    fi_n = calc_fi(n)
    new_exp = fi_n

    if are_relatively_prime(a, n):
        if m > fi_n:
            new_exp = m % fi_n
    else:
        new_exp = (m // (fi_n + 1)) + (m % (fi_n + 1))

    return calc_module(a, new_exp, n)


if __name__ == '__main__':
    res = calc_euler_module(26, 3369, 363)
    print(res)
