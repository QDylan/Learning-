# -*- coding: utf-8 -*-
"""
 @Time    : 2020-03-17 17:35
 @Author  : QDY
 @FileName: LinearList.py
 @Software: PyCharm
"""


class SequenceList:

    def __init__(self):
        self.SeqL = []

    def __str__(self):
        return str(self.SeqL)

    def isEmpty(self):
        return self.SeqL == []

    def input(self, elem):
        self.SeqL.append(elem)

    def size(self):
        return len(self.SeqL)


'''
栈： 后进先出
'''


class Stack(object):

    def __init__(self):
        self.__List = []

    def __str__(self):
        return str(self.__List)

    def isEmpty(self):
        return self.__List == []

    def push(self, elem):
        self.__List.append(elem)

    def size(self):
        return len(self.__List)

    def peek(self):
        if self.__List:
            return self.__List[-1]
        else:
            return None

    def pop(self):
        if self.__List:
            return self.__List.pop()
        else:
            return None


'''
队列：先进先出
'''


class Queue(object):

    def __init__(self):
        self.__List = []

    def __str__(self):
        return str(self.__List)

    def isEmpty(self):
        return self.__List == []

    def enqueue(self, elem):
        self.__List.insert(0, elem)

    def size(self):
        return len(self.__List)

    def head(self):
        if self.__List:
            return self.__List[-1]
        else:
            return None

    def dequeue(self):
        if self.__List:
            return self.__List.pop()
        else:
            return None


'''
双端队列
'''


class Deque(object):

    def __init__(self):
        self.__List = []

    def __str__(self):
        return str(self.__List)

    def isEmpty(self):
        return self.__List == []

    def add_front(self, elem):
        self.__List.insert(0, elem)

    def add_rear(self, elem):
        self.__List.append(elem)

    def remove_front(self):
        return self.__List.pop(0)

    def remove_rear(self):
        return self.__List.pop()

    def size(self):
        return len(self.__List)

    def front(self):
        if self.__List:
            return self.__List[0]
        else:
            return None

    def rear(self):
        if self.__List:
            return self.__List[-1]
        else:
            return None


class SingleList(object):
    """单链表"""

    # 定义结点内部类
    class __Node:
        def __init__(self, item=None, nxt=None):
            self.item = item
            self.next = nxt

    def __init__(self):
        self.__head = self.__Node(0, None)

    def __str__(self):
        cur = self.__head.next
        tmp = []
        while cur:
            tmp.append(cur.item)
            cur = cur.next
        return str(tmp)

    # 头插法
    def add(self, item):
        self.__head.next = self.__Node(item, self.__head.next)
        self.__head.item += 1

    # 尾插法
    def append(self, item):
        cur = self.__head
        while cur.next:
            cur = cur.next
        cur.next = self.__Node(item)
        self.__head.item += 1

    def insert(self, index, item):
        if index < 0:
            index = index + self.__head.item + 1
        cur = self.__head.next
        pre = self.__head
        pos = 0
        while pos < index:
            pos += 1
            pre = cur
            cur = cur.next

        pre.next = self.__Node(item, cur)
        self.__head.item += 1

    # 删除第一个item
    def remove(self, item):
        if not self.is_empty():
            cur = self.__head.next
            pre = self.__head
            index = 0
            while cur:
                if cur.item == item:
                    pre.next = cur.next
                    self.__head.item -= 1
                    del cur
                    return index
                pre = cur
                cur = cur.next
                index += 1
        return None

    def complete_remove(self, item):

        cur = self.__head.next
        pre = self.__head
        count = 0
        while cur:
            if cur.item == item:
                pre.next = cur.next
                count += 1
                self.__head.item -= 1
                cur = cur.next

                continue

            pre = cur
            cur = cur.next
        return count

    def pop(self, index=-1):
        if not self.is_empty():
            if index >= self.__head.item:
                return None
            if index < 0:
                index = index + self.__head.item
            cur = self.__head.next
            pre = self.__head
            pos = 0
            while pos < index:
                pos += 1
                pre = cur
                cur = cur.next
            pre.next = cur.next
            self.__head.item -= 1
            tmp = cur.item
            del cur
            return tmp
        return None

    # 找到元素第一个出现的位置
    def search(self, item):
        cur = self.__head.next
        index = 0
        while cur:
            if cur.item == item:
                return index
            index += 1
            cur = cur.next
        return None

    def length(self):
        return self.__head.item

    def is_empty(self):
        return self.__head.item == 0


class SingleCycleList(object):
    """单向循环链表"""

    class __Node(object):
        def __init__(self, item=None, nxt=None):
            self.item = item
            self.next = nxt

    def __init__(self):
        self.__head = self.__Node(0)

    def __str__(self):
        cur = self.__head.next
        tmp = []
        if not self.is_empty():
            while cur.next != self.__head.next:
                tmp.append(cur.item)
                cur = cur.next
            tmp.append(cur.item)
        return str(tmp)

    def is_empty(self):
        return self.__head.item == 0

    def length(self):
        return self.__head.item

    def add(self, item):
        if self.is_empty():
            self.__head.next = self.__Node(item)
            self.__head.next.next = self.__head.next
        else:
            cur = self.__head.next
            node = self.__Node(item, cur)
            while cur.next != self.__head.next:
                cur = cur.next
            cur.next = node
            self.__head.next = node
        self.__head.item += 1

    def append(self, item):
        node = self.__Node(item)
        if self.is_empty():
            self.__head.next = node
            node.next = self.__head.next
        else:
            cur = self.__head.next
            while cur.next != self.__head.next:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.__head.item += 1

    def insert(self, index, item):
        if index < 0:
            index = index + self.__head.item + 1
        if index == 0:
            self.add(item)
        elif index >= self.__head.item:
            self.append(item)
        else:

            cur = self.__head.next
            pre = self.__head
            pos = 0
            while pos < index:
                pre = cur
                cur = cur.next
                pos += 1
            pre.next = self.__Node(item, cur)

            self.__head.item += 1

    def search(self, item):
        cur = self.__head.next
        index = 0
        while cur.next != self.__head.next:
            if cur.item == item:
                return index
            cur = cur.next
            index += 1
        if cur.item == item:
            return index

        return None

    def remove(self, item):
        cur = self.__head.next
        pre = self.__head
        index = 0
        if cur.item == item:  # 头节点

            if self.__head.item == 1:
                self.__head.next = None
            else:
                while cur.next != self.__head.next:
                    cur = cur.next
                self.__head.next = pre.next.next
                cur.next = self.__head.next
            self.__head.item -= 1
            return index
        while index < self.__head.item:
            if cur.item == item:
                pre.next = cur.next
                self.__head.item -= 1
                return index
            pre = pre.next
            cur = cur.next
            index += 1
        return None

    def pop(self, index=-1):
        if index < 0:
            index = index + self.__head.item
        elif index >= self.__head.item:
            return None

        cur = self.__head.next
        pre = self.__head
        if index == 0:
            if self.__head.item == 1:
                self.__head.next = None
                self.__head.item -= 1
                return cur.item
            item = cur.item
            while cur.next != self.__head.next:
                cur = cur.next
            cur.next = self.__head.next.next
            self.__head.next = pre.next.next
            self.__head.item -= 1
            return item
        pos = 0
        while pos < index:
            cur = cur.next
            pre = pre.next
            pos += 1
        pre.next = cur.next
        self.__head.item -= 1
        return cur.item


class DoubleList(object):
    """双链表"""
    class __Node(object):

        def __init__(self, item=None, prev=None, nxt=None):
            self.prev = prev
            self.item = item
            self.next = nxt

    def __init__(self):
        self.__head = self.__Node()
        self.__head.item = 0

    def __str__(self):
        tmp = []
        cur = self.__head.next
        while cur:
            tmp.append(cur.item)
            cur = cur.next
        return str(tmp)

    def is_empty(self):
        return self.__head.next is None

    def length(self):
        return self.__head.item

    def add(self, item):
        node = self.__Node(item=item, prev=None, nxt=self.__head.next)
        if self.__head.item != 0:
            node.next.prev = node

        self.__head.next = node
        self.__head.item += 1

    def append(self, item):
        cur = self.__head
        while cur.next:
            cur = cur.next
        cur.next = self.__Node(item=item, prev=cur, nxt=None)
        self.__head.item += 1

    def insert(self, index, item):
        if index < 0:
            index = index + self.__head.item + 1
        if index >= self.__head.item:
            self.append(item)
        elif index == 0:
            self.add(item)
        else:
            cur = self.__head.next
            pos = 0
            while pos < index:
                cur = cur.next
                pos += 1
            node = self.__Node(item=item, prev=cur.prev, nxt=cur)
            cur.prev.next = node
            cur.prev = node
            self.__head.item += 1

    def remove(self, item):
        pos = 0
        cur = self.__head.next
        while cur:
            if cur.item == item:

                if pos == 0:
                    self.__head.next = cur.next
                elif pos == self.__head.item-1:
                    cur.prev.next = cur.next
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev

                self.__head.item -= 1
                return pos
            cur = cur.next
            pos += 1

        return None


class DoubleCycleList(object):
    """双循环链表"""
    class __Node(object):

        def __init__(self, item=None, prev=None, nxt=None):
            self.prev = prev
            self.item = item
            self.next = nxt

    def __init__(self):
        self.__head = self.__Node()
        self.__head.item = 0

    def __str__(self):
        cur = self.__head.next
        tmp = []
        if not self.is_empty():
            while cur.next != self.__head.next:
                tmp.append(cur.item)
                cur = cur.next
            tmp.append(cur.item)
        return str(tmp)

    def is_empty(self):
        return self.__head.next is None

    def length(self):
        return self.__head.item

    def add(self, item):
        node = self.__Node(item=item, nxt=self.__head.next)
        if self.is_empty():
            self.__head.next = node
            node.next = node
        else:
            cur = self.__head.next
            while cur.next != self.__head.next:
                cur = cur.next
            cur.next = node
            self.__head.next = node
            node.next.prev = node

        self.__head.item += 1

    def append(self, item):
        node = self.__Node(item=item, prev=None, nxt=self.__head.next)
        if self.is_empty():
            self.__head.next = node
            node.next = node
        else:
            cur = self.__head.next
            while cur.next != self.__head.next:
                cur = cur.next
            node.prev = cur
            cur.next = node

        self.__head.item += 1

    def insert(self, index, item):
        if index < 0:
            index = index + self.__head.item + 1
        if index >= self.__head.item:
            self.append(item)
        elif index == 0:
            self.add(item)
        else:
            cur = self.__head.next
            pos = 0
            while pos < index:
                cur = cur.next
                pos += 1
            node = self.__Node(item=item, prev=cur.prev, nxt=cur)
            cur.prev.next = node
            cur.prev = node
            self.__head.item += 1

    def remove(self, item):
        pos = 0
        cur = self.__head.next
        while pos < self.__head.item:
            if cur.item == item:
                if pos == 0:
                    if self.__head.item > 1:
                        while cur.next != self.__head.next:
                            cur = cur.next
                        self.__head.next.next.prev = None
                        cur.next = self.__head.next.next
                        self.__head.next = self.__head.next.next
                    else:
                        self.__head.next = None
                elif pos == self.__head.item-1:
                    cur.prev.next = cur.next
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev

                self.__head.item -= 1
                return pos
            cur = cur.next
            pos += 1

        return None


if __name__ == '__main__':
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # print(s.pop(), s.pop(), s.peek())
    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)
    # q.enqueue(5)
    # print(q.dequeue(), q.dequeue(), q.head())
    # sl = SingleList()
    # sl.append(1)
    # # print(sl.isEmpty())
    # sl.add(-1)
    # sl.append(2)
    # sl.add(-2)
    # print(sl, sl.length())  # -2 -1 1 2
    # sl.remove(-2)
    # sl.remove(1)
    # print(sl, sl.length())  # -1 2
    # sl.insert(0, -3)
    # sl.insert(3, 3)
    # sl.insert(2, 0)
    # sl.insert(2, 0)
    # sl.insert(-1, 0)
    # print(sl, sl.length())  # -3 -1 0 0 2 3 0
    # sl.pop()
    # sl.pop(0)
    # print(sl, sl.length())
    # print(sl.search(2))
    # print(sl.complete_remove(0), sl, sl.length())
    print('----------------------------------')
    scl = SingleCycleList()
    print(scl.is_empty(), scl)
    scl.append(4)
    scl.add(3)
    scl.add(2)
    scl.add(1)
    scl.append(5)
    scl.append(5)
    print(scl, scl.length())  # [1, 2, 3, 4, 5, 5] 6
    print(scl.search(1), scl.search(5))  # 0 4
    scl.insert(0, 0.5)
    scl.insert(3, 2.5)
    scl.insert(-1, 6)
    print(scl, scl.length())  # [0.5, 1, 2, 2.5, 3, 4, 5, 5, 6] 9
    print(scl.remove(5), scl, scl.length())
    print(scl.remove(0.5), scl, scl.length())
    print(scl.pop(), scl, scl.length())
    print(scl.pop(0), scl, scl.length())
    print(scl.pop(1), scl, scl.length())
    print('----------------------------------')
    dl = DoubleList()
    print(dl.is_empty(), dl)
    dl.append(4)
    dl.add(3)
    dl.add(2)
    dl.add(1)
    dl.append(5)
    dl.append(5)
    print(dl.is_empty(), dl, dl.length())
    dl.insert(0, 0.5)
    dl.insert(3, 2.5)
    dl.insert(-1, 6)
    print(dl, dl.length())
    print(dl.remove(5), dl, dl.length())
    print(dl.remove(0.5), dl, dl.length())
    print(dl.remove(6), dl, dl.length())
    print('-----------------------------------')
    dcl = DoubleCycleList()
    print(dcl.is_empty(), dcl)
    dcl.append(4)
    dcl.add(3)
    dcl.add(2)
    dcl.add(1)
    dcl.append(5)
    dcl.append(5)
    dcl.insert(0, 0.5)
    dcl.insert(3, 2.5)
    dcl.insert(-1, 6)
    print(dcl.is_empty(), dcl, dcl.length())
    print(dcl.remove(5), dcl, dcl.length())
    print(dcl.remove(0.5), dcl, dcl.length())
    print(dcl.remove(6), dcl, dcl.length())
    print(dcl.remove(5), dcl, dcl.length())
    print(dcl.remove(2.5), dcl, dcl.length())
    print(dcl.remove(3), dcl, dcl.length())
    print(dcl.remove(2), dcl, dcl.length())
    print(dcl.remove(1), dcl, dcl.length())
    print(dcl.remove(4), dcl, dcl.length())