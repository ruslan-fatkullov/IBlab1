from typing import TextIO

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
    for _ in range(100):
        temp = generic_symbol(temp)
        result_list_of_numbers.append(format(temp, 'b'))
    result_string = ""
    list_of_chars = list(result_string.join(result_list_of_numbers))
    print(result_list_of_numbers)
    print(list_of_chars)
    ert = "".join(list_of_chars)
    file2 = open("source/second.txt", "w")
    file2.write(ert)
    file2.close()
    print("Последовательность случайна") if first_lab.frequency_test(list_of_chars) else print("Последовательность НЕ "
                                                                                            "случайна")
