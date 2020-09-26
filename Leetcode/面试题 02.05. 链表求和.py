# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-26 18:53
 @Author  : QDY
 @FileName: 面试题 02.05. 链表求和.py
 @Software: PyCharm
"""
"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912

进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?
(反转两个链表，将最后得到的链表再反转一次)

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        head = ListNode(None)
        cur, carry = head, 0
        while cur1 or cur2:
            num1 = num2 = 0
            if cur1:
                num1 = cur1.val
                cur1 = cur1.next
            if cur2:
                num2 = cur2.val
                cur2 = cur2.next
            num = num1 + num2 + carry
            cur.next = ListNode(num % 10)
            carry = num // 10
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return head.next
