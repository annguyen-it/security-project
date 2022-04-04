from Chapter3.e1_ha_bac import calc_module
from Chapter3.e2_extended_euclid import calc_extended_euclid


def public_key(p: int, q: int, e: int) -> (int, int):
    n = p * q
    return e, n


def private_key(p: int, q: int, e: int) -> (int, int):
    n = p * q
    fi_n = (p - 1) * (q - 1)
    d = calc_extended_euclid(e, fi_n)
    return d, n


def rsa_authentication_encrypt(p: int, q: int, e: int, plain_text: int) -> int:
    d, n = private_key(p, q, e)
    cypher_text = calc_module(plain_text, d, n)
    return cypher_text


def rsa_authentication_decrypt(p: int, q: int, e: int, cypher_text: int) -> int:
    e, n = public_key(p, q, e)
    plain_text = calc_module(cypher_text, e, n)
    return plain_text


def rsa_confidentiality_encrypt(p: int, q: int, e: int, plain_text: int) -> int:
    e, n = public_key(p, q, e)
    cypher_text = calc_module(plain_text, e, n)
    return cypher_text


def rsa_confidentiality_decrypt(p: int, q: int, e: int, cypher_text: int) -> int:
    d, n = private_key(p, q, e)
    plain_text = calc_module(cypher_text, d, n)
    return plain_text


if __name__ == '__main__':
    m, p, q, e = 47, 37, 59, 53
    enc = rsa_authentication_encrypt(p, q, e, m)
    dec = rsa_authentication_decrypt(p, q, e, enc)
    print(enc)
    print(dec)

    enc = rsa_confidentiality_encrypt(p, q, e, m)
    dec = rsa_confidentiality_decrypt(p, q, e, enc)
    print(enc)
    print(dec)
