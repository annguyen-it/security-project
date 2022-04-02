import string

alphabet = string.ascii_lowercase


def encrypt(plain_text: str, k: int) -> str:
    cypher_text = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        index_in_alphabet = (alphabet.index(current_char) + k) % 26
        cypher_text += alphabet[index_in_alphabet]
    return cypher_text


def decrypt(cypher_text: str, k: int) -> str:
    plain_text = ''
    for i in range(len(cypher_text)):
        current_char = cypher_text[i]
        index_in_alphabet = (alphabet.index(current_char) - k) % 26
        plain_text += alphabet[index_in_alphabet]
    return plain_text


if __name__ == '__main__':
    result = encrypt('abcd', 2)
    print(result)
    result2 = decrypt(result, 2)
    print(result2)
