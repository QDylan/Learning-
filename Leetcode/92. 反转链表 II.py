# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/14 10:35
 @Author  : QDY
 @FileName: 92. 反转链表 II.py
 @Software: PyCharm
"""
"""
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    
    说明:
    1 ≤m≤n≤ 链表长度。
    
    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m: int, n: int):
        if not head or not head.next or m == n: return head
        head_ = ListNode(None)
        head_.next = head
        prev, cur, index = head_, head, 1
        while cur.next and index < m:
            cur, prev = cur.next, prev.next
            index += 1
        tmp_head = prev
        cur, prev = cur.next, prev.next

        while cur and index < n:
            nxt = cur.next
            cur.next = prev
            cur, prev = nxt, cur
            index += 1
        tmp_head.next.next = cur
        tmp_head.next = prev
        return head_.next
