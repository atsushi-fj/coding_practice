"""
Input: 'This is a pen. This is an apple. Applepen.'
最も出現回数の多い文字をカウントする
Output: ('p', 6)
"""

import operator
from typing import Tuple


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]  # ループないでappendするものは内包表記でかく
    return max(l, key=operator.itemgetter(1))  # タプルのインデックス1をキーとして最大値


def count_chars_v2(strings: str) -> Tuple[str, int]:  # カウント系はdictionaryを使う
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1  # charのvalue（ないときは0で初期化） + 1
    max_key = max(d, key=d.get)  # 辞書のvalueの最大値
    return max_key, d[max_key]


if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(s))
    print(count_chars_v2(s))

