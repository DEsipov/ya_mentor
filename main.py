#!-*-coding:utf-8-*-

"""
Задача 1. Даны два списка, нужно вернуть элементы,
которые есть в 1-ом списке, но нет во 2-ом.
Оценить эффективность своего решения.
"""


def foo(array_1: set, array_2: set) -> set:
    return array_1 - array_2


if __name__ == '__main__':
    arr_1 = {1, 2, 3}
    arr_2 = {2, 3}

    res = foo(arr_1, arr_2)

    print(f'Result: {res}')
