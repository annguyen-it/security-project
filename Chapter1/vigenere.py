import string

alphabet = string.ascii_lowercase


def init_key(key: str, plain_text: str, repeat: bool) -> str:
    global result
    result = key

    if repeat:
        while len(result) < len(plain_text):
            result += key
        return result[:len(plain_text) + 1]

    return (key + plain_text)[:len(plain_text) + 1]


def encrypt(plain_text: str, k: str) -> str:
    cypher_text = ''
    for i in range(len(plain_text)):
        index_in_alphabet = (alphabet.index(plain_text[i]) + alphabet.index(k[i])) % 26
        cypher_text += alphabet[index_in_alphabet]
    return cypher_text


def decrypt(cypher_text: str, k: str) -> str:
    plain_text = ''
    for i in range(len(cypher_text)):
        index_in_alphabet = (alphabet.index(cypher_text[i]) - alphabet.index(k[i])) % 26
        new_char = alphabet[index_in_alphabet]
        k += new_char
        plain_text += new_char
    return plain_text


if __name__ == '__main__':
    text = 'moneymakesth'
    d_key = init_key('nopain', text, False)

    result = encrypt(text, d_key)
    print(result)
    result2 = decrypt(result, d_key)
    print(result2)
