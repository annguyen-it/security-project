import math
import string
import textwrap


def encrypt(plain_text: str, k: int) -> str:
    cypher_text = ''
    groups = textwrap.wrap(plain_text, k)
    for i in range(k):
        for item in groups:
            if i >= len(item):
                break
            cypher_text += item[i]
    return cypher_text


def decrypt(cypher_text: str, k: int) -> str:
    plain_text = ''
    groups = [[] for _ in range(k)]
    max_in_group = math.ceil(len(cypher_text) / k)
    special_rows = len(cypher_text) % k
    row = 0

    for i in range(len(cypher_text)):
        groups[row].append(cypher_text[i])
        if len(groups[row]) == max_in_group:
            row += 1
        elif len(groups[row]) == max_in_group - 1 and row >= special_rows:
            row += 1

    for i in range(k):
        for item in groups:
            if i >= len(item):
                break
            plain_text += item[i]
    return plain_text


if __name__ == '__main__':
    alphabet = string.ascii_lowercase
    key = 8
    result = encrypt('donttroubletrouble', key)
    print(result)
    result2 = decrypt(result, key)
    print(result2)
