"""
Input
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20...]

Prime number
[2, 3, 5, 7, 11, 13, 17, 19]  : True

Non prime number
[1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]  : False
"""

import math
import random
import time


def is_prime_v1(num: int) -> bool:
    if type(num) is not int:
        return False

    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


""" 例えば入力値３６に対して
36 = 1 * 36　２つの因数に分解してみると
36 = 2 * 18
36 = 3 * 12
36 = 4 * 9
36 = 6 * 6 <=> root(n)
36 = 9 * 4　　
36 = 12 * 3
36 = 18 * 2
36 = 36 * 1
"""


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def is_prime_v2_1(num: int) -> bool:
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


# 偶数は2を除いて全て素数ではない


def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


"""
2か3の倍数は2,3を除いて素数ではない。
6の倍数の±1は素数ではない。それ以外は素数。
"""


def is_prime_v4(num: int) -> bool:
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(1000000)]

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print(time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print(time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2_1(num)
    print(time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print(time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v4(num)
    print(time.time() - start)