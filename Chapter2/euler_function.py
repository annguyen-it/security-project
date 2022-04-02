from functions import is_prime


def calc_fi(n: int) -> int:
    if is_prime(n):
        return n - 1

    prime_numbers = dict()
    current_division = 2
    while n > 1:
        if n % current_division == 0:
            prime_numbers[current_division] = prime_numbers[current_division] + 1 \
                if current_division in prime_numbers.keys() \
                else 1
            n /= current_division
        else:
            current_division += 1

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
