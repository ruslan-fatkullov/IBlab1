import rsa
import math


def init():
    print("Лабораторная работа №5")
    # 1) RSA 2) тест Лемана

    (publicKey, privateKey) = rsa.newkeys(32)
    print(publicKey.n)
    print(publicKey.e)
    print(privateKey.n)
    print(privateKey.e)
    print(privateKey.d)

    f = open("source/originalText5.txt", 'r')
    message = f.read()

    list_message = list(message)
    print(list_message)
    new_list = list()
    for i in list_message:
        new_list.append(ord(i))
    print(new_list)



    for i in range(len(new_list)):
        new_list[i] = pow(new_list[i], publicKey.e) % publicKey.n
    print(new_list)
    print("done")

    enc = ""
    for i in new_list:
        enc += str(i) + " "

    file = open('source/codeText5.txt', 'w')
    file.write(enc)
    file.close()


    decypt_list = list()
    for i in range(len(new_list)):
        temp = chr(pow(new_list[i], privateKey.d) % privateKey.n)
        decypt_list.append(temp)
    out = "".join(decypt_list)
    print(out)

