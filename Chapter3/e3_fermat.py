from Chapter3.e1_ha_bac import calc_module


# a^(p-1) mod p = 1
def calc_fermat_module(a: int, m: int, p: int) -> int:
    new_exp = m
    if m > p:
        new_exp = m % (p - 1)
    return calc_module(a, new_exp, p)


if __name__ == '__main__':
    res = calc_fermat_module(277, 6863, 6863)
    print(res)
