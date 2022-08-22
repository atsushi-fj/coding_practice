"""
順列を表示
Input [1, 2, 3]
Output [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
"""

from typing import List


def all_perms_v1(elements: List[int]) -> List[List[int]]:
    result = []

    if len(elements) <= 1:
        return [elements]

    for perm in all_perms_v1(elements[1:]):  # perm <= [[2, 3], [3]]  elements <= [[1, 2, 3], [2, 3]]
        for i in range(len(elements)):
            result.append(perm[:i] + elements[0:1] + perm[i:])
    return result


def all_perms_v2(elements: List[int]) -> List[List[int]]:
    if len(elements) <= 1:
        yield elements
    else:  # yieldの時はプログラムが止まらない
        for perm in all_perms_v2(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == '__main__':
    for p in all_perms_v1([1, 2, 3]):
        print(p)

    print('########################################')

    for p in all_perms_v2([1, 2, 3]):
        print(p)
