import random


def crypt(message, key):
    n = len(message)
    d = n % 6
    add = []
    if d != 0:
        add = [chr(random.randrange(ord('a'), ord('z'), 1)) for _ in range(6 - d)]
    message += ''.join(add)
    result_string = ""
    for i in range(0, n, 6):
        string = [message[i+j] for j in range(6)]
        substring = ""
        for j in range(3):
            substring += string[key[j]*2]
            substring += string[key[j]*2+1]
        result_string += substring
    return result_string


def decrypt(code):
    n = len(code)
    for i in range(0, n, 6):
        substring = []


def bin2dec():
    pass


def init():
    print("Лабораторная работа №4")
    mes = "I would like to read some characters from a string s1 and put it into another string s2"
    key = [2, 0, 1]
    res = crypt(mes, key)
    print(res)
    decrypt(res)
