from Chapter3.e1_ha_bac import calc_module
from Chapter3.e2_extended_euclid import calc_extended_euclid


def public_key(_a: int, _xa: int, _q: int) -> int:
    return calc_module(_a, _xa, _q)


def el_gamal_encrypt(_m: int, _k: int, _q: int, _a: int, _xa: int) -> (int, int):
    ya = public_key(_a, _xa, _q)

    K = calc_module(ya, _k, _q)
    _c1 = calc_module(_a, _k, _q)
    _c2 = K * _m % _q
    return _c1, _c2


def el_gamal_decrypt(_c1: int, _c2: int, _q: int, _xa: int) -> int:
    K = calc_module(_c1, _xa, _q)
    _m = calc_extended_euclid(K, _q) * _c2 % _q
    return _m


if __name__ == '__main__':
    q, a, xa, k, m = 6571, 3, 436, 979, 459
    c1, c2 = el_gamal_encrypt(m, k, q, a, xa)
    dec = el_gamal_decrypt(c1, c2, q, xa)

    print(c1, c2)
    print(dec)
