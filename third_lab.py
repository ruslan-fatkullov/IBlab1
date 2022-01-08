import hashlib

def init():
    print("Лабораторная работа №3")
    file = open("source/second.txt", "r")
    data = file.read()
    print(data)
    hash_object = hashlib.md5(data)
    print(hash_object.hexdigest())