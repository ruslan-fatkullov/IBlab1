import first_lab
import time
import math


def generic_symbol(x):
    x = (1664525 * x + 1013904223) % math.pow(2, 32)
    return int(x)


def init():
    print("Вторая лабораторная работа")
    result_list_of_numbers = list()
    temp = int(time.time())
    print(temp)
    for _ in range(10):
        temp = generic_symbol(temp)
        result_list_of_numbers.append(format(temp, 'b'))
    result_string = ""
    list_of_chars = list(result_string.join(result_list_of_numbers))
    print(result_list_of_numbers)
    print(list_of_chars)
    file = open('second.txt', 'w')
    file.write(result_string.join(result_list_of_numbers))
    file.close()
    print("Последовательность случайна") if first_lab.frequency_test(list_of_chars) else print("Последовательность НЕ "
                                                                                            "случайна")
