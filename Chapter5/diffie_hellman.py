from Chapter3.e1_ha_bac import calc_module


def diffie_hellman(q: int, a: int, xa: int, xb: int):
    # An
    # Khóa công khai
    ya = calc_module(a, xa, q)

    # Khóa phiên
    ka = calc_module(ya, xb, q)

    # Ba
    # Khóa công khai
    yb = calc_module(a, xb, q)

    # Khóa phiên
    kb = calc_module(yb, xa, q)

    return ya, yb, ka, kb


if __name__ == '__main__':
    print(diffie_hellman(7159, 3, 371, 476))
