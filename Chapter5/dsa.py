import random

from Chapter3.e1_ha_bac import calc_module
from Chapter3.e2_extended_euclid import calc_extended_euclid


def public_key(p: int, q: int, h: int, xa: int) -> (int, int):
    g = calc_module(h, (p - 1) // q, p)
    ya = calc_module(g, xa, p)
    return ya, g


def dsa_encrypt(p: int, q: int, h: int, xa: int, k: int, hm: int) -> (int, int):
    ya, g = public_key(p, q, h, xa)
    r = calc_module(g, k, p) % q
    s = calc_extended_euclid(k, q) * (hm + xa * r) % q
    return r, s


def dsa_decrypt(p: int, q: int, h: int, xa: int, hm: int, r: int, s: int) -> bool:
    ya, g = public_key(p, q, h, xa)
    w = calc_extended_euclid(s, q)
    u1 = hm * w % q
    u2 = r * w % q
    v = calc_module(g, u1, p) * calc_module(ya, u2, p) % p % q
    return v == r


if __name__ == '__main__':
    _p, _q, _h, x_a, _k, _hm = 59, 29, 3, 19, 25, random.randint(0, 1000)
    _r, _s = dsa_encrypt(_p, _q, _h, x_a, _k, _hm)
    dec = dsa_decrypt(_p, _q, _h, x_a, _hm, _r, _s)
    print(_r, _s)
    print(dec)
