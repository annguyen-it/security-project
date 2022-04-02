from functions import is_prime, analysis


def calc_fi(n: int) -> int:
    if is_prime(n):
        return n - 1

    prime_numbers = analysis(n)

    result = 1
    for num in prime_numbers:
        exp = prime_numbers[num]
        if exp > 1:
            result *= pow(num, exp) - pow(num, exp - 1)
        else:
            result *= num - 1
    return result


if __name__ == '__main__':
    res = calc_fi(2856)
    print(res)
