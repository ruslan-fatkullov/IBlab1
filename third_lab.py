import hashlib

def init():
    print("Лабораторная работа №3")
    hash_object = hashlib.md5(b'fdg dfg')
    print(hash_object.hexdigest())