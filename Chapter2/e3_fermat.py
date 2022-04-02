from Chapter2.e1_ha_bac import calc_module


def calc_fermat_module(a: int, m: int, n: int) -> int:
    new_exp = m
    if m > n:
        new_exp = m % (n - 1)
    return calc_module(a, new_exp, n)


if __name__ == '__main__':
    res = calc_fermat_module(277, 6863, 6863)
    print(res)
