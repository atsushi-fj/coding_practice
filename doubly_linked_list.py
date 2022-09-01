from __future__ import annotations
from typing import Any, Optional


class Node(object):

    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any):  # 末尾に追加
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:  # 先頭にデータを挿入
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:  # 一覧表示
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:  # 先頭から見て該当するものを削除
        current_node = self.head

        if current_node and current_node.data == data:  # 先頭を削除
            if current_node.next is None:  # 要素が1個だけのとき
                current_node = None
                self.head = None
                return
            else:  # 要素が複数あるとき
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = None
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:  # 削除するものがないとき
            return

        if current_node.next is None:  # 末尾を削除するとき
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        else:  # 真ん中を削除するとき
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self) -> None:  # 逆順
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            current_node = current_node.prev

        if previous_node:  # ループを1回でもしたとき
            self.head = previous_node.prev

    def reverse_recursive(self) -> None:  # 逆順
        def _reverse_recursive(current_node: Node) -> Optional[Node]:  # NoneかNodeがかえる
            if not current_node:  # 何もないとき
                return None  # self.head = None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            if not current_node.prev:
                return current_node

            return _reverse_recursive(current_node.prev)  # current_node = current_node.prev

        self.head = _reverse_recursive(self.head)

    def sort(self) -> None:  # 昇順にソートする
        if self.head is None:
            return

        current_node = self.head
        while current_node:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(0)
    d.append(5)
    d.append(2)
    d.insert(1)
    d.insert(9)
    d.print()

    print('##############################')

    d.reverse_iterative()
    d.print()

    print('##############################')

    d.reverse_recursive()
    d.print()

    print('##############################')

    d.remove(2)
    d.print()

    print('#############################')

    d.sort()
    d.print()





