import random
import math
import time
import first_lab
import second_lab
import third_lab
import four_lab
import five_lab

if __name__ == '__main__':
    print("Выберете лабораторную работу для выполнения: "
          "\n'1' - первая лабораторная "
          "\n'2' - вторая лабораторная "
          "\n'3' - третья лабораторная "
          "\n'0' - выйти")
    lab_num = ""
    while lab_num != "0":
        print("введите номер")
        lab_num = input()
        if lab_num == "1":
            first_lab.init()
        elif lab_num == "2":
            second_lab.init()
        elif lab_num == "3":
            third_lab.init()
        elif lab_num == "4":
            four_lab.init()
        elif lab_num == "5":
            five_lab.init()
        elif lab_num == "0":
            break
        else:
            print("Неккоректное значение")

    # print("Enter the size of string: ")
    # size_of_string = input()
    # generate_file(int(size_of_string), "testFile")
    # str_to_list = read_file("testFile")
    # for i in range(len(str_to_list)):
    #     str_to_list[i] = 2 * int(str_to_list[i]) - 1
    # print(str_to_list)
    # print(frequency_test(str_to_list))
    #
    # result_str = list()
    # temp = int(time.time())
    # print(temp)
    # for _ in range(10000):
    #     temp = generic_symbol(temp)
    #     result_str.append((temp % 10) // 5)
    # print(result_str)
    # print(frequency_test(result_str))
