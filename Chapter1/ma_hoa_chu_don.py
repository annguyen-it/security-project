import string

alphabet = string.ascii_lowercase


def encrypt(plain_text: str, k: str) -> str:
    cypher_text = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        index_in_alphabet = alphabet.index(current_char)
        cypher_text += k[index_in_alphabet]
    return cypher_text


def decrypt(cypher_text: str, k: str) -> str:
    plain_text = ''
    for i in range(len(cypher_text)):
        current_char = cypher_text[i]
        index_in_key = k.index(current_char)
        plain_text += alphabet[index_in_key]
    return plain_text


if __name__ == '__main__':
    key = 'qwertyuiopasdfghjklzxcvbnm'
    result = encrypt('abcd', key)
    print(result)
    result2 = decrypt(result, key)
    print(result2)
