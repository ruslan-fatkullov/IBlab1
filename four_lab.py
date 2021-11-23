import random


def crypt_message(message, m, n):
    string_len = len(message)
    d = string_len % 6
    add = []
    if d != 0:
        add = [chr(random.randrange(ord('a'), ord('z'), 1)) for _ in range(6 - d)]
    message += ''.join(add)
    result_string = ""
    for i in range(0, string_len, 6):
        string = [message[i + j] for j in range(6)]
        substring = ""
        for j in range(n, 6):
            substring += string[j]
        result_string += substring
        substring = ""
        for j in range(0, m):
            substring += string[j]
        result_string += substring
        substring = ""
        for j in range(m, n):
            substring += string[j]
        result_string += substring

    return result_string


def decrypt_message(code, m, n):
    string_len = len(code)
    decode_string = ""
    for i in range(0, string_len, 6):
        string = [code[i + j] for j in range(6)]
        for j in range(n, 6):
            decode_string += string[j]
        for j in range(0, m):
            decode_string += string[j]
        for j in range(m, n):
            decode_string += string[j]
    return decode_string


def crypt(iteration_count, message, m, n):
    res = message
    # print(m)
    # print(n)
    for i in range(iteration_count):
        res = crypt_message(res, m[i], n[i])
        # print(str(i+1) + " " + res)
    return res


def decrypt(iteration_count, message, m, n):
    res = message
    # print(m)
    # print(n)
    for i in range(iteration_count):
        res = decrypt_message(res, m[i], n[i])
        # print(res)
    return res


def init():
    print("Лабораторная работа №4")
    print("Введите строку для шифрования")
    f = open("originalText.txt", 'r')
    mes = f.read()
    m = [2, 1, 1]
    n = [4, 3, 2]
    result = crypt(3, mes, m, n)
    # decode = decrypt_message(result, 2, 4)
    # print(decode)
    m.reverse()
    n.reverse()
    decode = decrypt(3, result, m, n)
    print("Защифрованный текст")
    print(result)
    file = open('codeText.txt', 'w')
    file.write(result)
    file.close()
    print("Дешифрованный текст")
    print(decode)
    file = open('decodeText.txt', 'w')
    file.write(decode)
    file.close()
