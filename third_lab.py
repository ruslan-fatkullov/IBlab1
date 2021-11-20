import hashlib

def init():
    print("Лабораторная работа №3")
    hash_object = hashlib.md5(b'HELLO WORLD')
    print(hash_object.hexdigest())