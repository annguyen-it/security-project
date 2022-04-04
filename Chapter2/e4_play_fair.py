import string

alphabet = string.ascii_lowercase
key_mat = [[] for _ in range(5)]


def find_in_key_mat(c: str) -> (int, int):
    for row in range(5):
        for col in range(5):
            if c == key_mat[row][col]:
                return row, col
            if c == 'j' and key_mat[row][col] == 'i':
                return row, col


def insert_key_mat(c: str, row: int) -> int:
    if c == 'j':
        return row
    key_mat[row].append(c)
    if len(key_mat[row]) == 5:
        row += 1
    return row


def init_key_mat(k: str) -> None:
    char_in_key = set()
    n_k = k + alphabet
    row = 0

    for c in n_k:
        if c not in char_in_key:
            if c == 'j':
                if 'i' not in char_in_key:
                    char_in_key.add('i')
                    row = insert_key_mat('i', row)
            else:
                char_in_key.add(c)
                row = insert_key_mat(c, row)


def encrypt(plain_text: str, k: str) -> str:
    cypher_text = ''
    i = 0
    char_pair = []
    for _ in range(len(plain_text)):
        if plain_text[i] != plain_text[i + 1]:
            char_pair.append(plain_text[i] + plain_text[i + 1])
        else:
            char_extra = 'x' if plain_text[i] != 'x' else 'b'
            plain_text = plain_text[:i + 1] + char_extra + plain_text[i + 1:]
            char_pair.append(plain_text[i] + plain_text[i + 1])
        i += 2
        if i == len(plain_text) - 1:
            char_extra = 'x' if plain_text[i] != 'x' else 'b'
            char_pair.append(plain_text[i] + char_extra)
            break
        elif i > len(plain_text) - 1:
            break

    for pair in char_pair:
        p0 = find_in_key_mat(pair[0])
        p1 = find_in_key_mat(pair[1])

        if p0[0] == p1[0]:
            row = p0[0]
            new_col_0 = (p0[1] + 1) % 5
            new_col_1 = (p1[1] + 1) % 5
            cypher_text += key_mat[row][new_col_0] + key_mat[row][new_col_1]
        elif p0[1] == p1[1]:
            col = p0[1]
            new_row_0 = (p0[0] + 1) % 5
            new_row_1 = (p1[0] + 1) % 5
            cypher_text += key_mat[new_row_0][col] + key_mat[new_row_1][col]
        else:
            cypher_text += key_mat[p0[0]][p1[1]] + key_mat[p1[0]][p0[1]]
            print(cypher_text)

    return cypher_text


def decrypt(cypher_text: str, k: str) -> str:
    plain_text = ''
    for i in range(len(cypher_text)):
        current_char = cypher_text[i]
        index_in_key = k.index(current_char)
        plain_text += alphabet[index_in_key]
    return plain_text


if __name__ == '__main__':
    key = 'monarchy'
    init_key_mat(key)

    result = encrypt('balloon', key)
    print(result)
    # result2 = decrypt(result, key)
    # print(result2)
