def calc_module(a: int, m: int, n: int) -> int:
    if m == 1:
        return a % n
    if m % 2 == 0:
        return calc_module((a * a) % n, m // 2, n)
    return (calc_module((a * a) % n, m // 2, n) * a) % n


if __name__ == '__main__':
    res = calc_module(999, 450, 10301)
    print(res)
