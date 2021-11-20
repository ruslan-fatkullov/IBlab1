import random
import math


def generate_binary_file(file_size, file_name):
    generic_string = ""
    for _ in range(file_size):
        generic_string += random.randint(0, 1).__str__()
    file = open(f'{file_name}.txt', 'w')
    file.write(generic_string)
    file.close()


def frequency_test(string_for_check):
    for i in range(len(string_for_check)):
        string_for_check[i] = 2 * int(string_for_check[i]) - 1
    return abs(sum(string_for_check)) / math.sqrt(len(string_for_check)) <= 1.82138636


def read_file(reading_file):
    f = open(f"{reading_file}.txt", 'r')
    str_to_list = list(f.read())
    return str_to_list


def init():
    print("Первая лабораторная")
    while True:
        print("Введите размер файла:")
        file_size = input()
        generate_binary_file(int(file_size), "test")
        result = read_file("test")
        print(result)
        x: str = "Последовательность является случайной" if frequency_test(result) else "Последовательность не случайна"
        print(x)
        print("'любая клавиша' - сгенерировать новый файл '0' - закончить")
        end = input()
        if end == '0':
            break
