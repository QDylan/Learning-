# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/15 10:32
 @Author  : QDY
 @FileName: 143. 重排链表.py
 @Software: PyCharm
"""
"""
    给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
    将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

    示例 1:
    给定链表 1->2->3->4, 重新排列为 1->4->2->3.

    示例 2:
    给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        length, cur = 0, head
        while cur:
            length += 1
            cur = cur.next
        mid = length // 2
        index, cur = 0, head
        while index < mid:  # 定位到中间节点
            cur = cur.next
            index += 1
        prev, cur = cur, cur.next
        prev.next = None
        while cur:  # 翻转后面的链表
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        left, right = head, prev
        while left.next and right.next:
            right_nxt = right.next
            left.next, right.next = right, left.next
            left, right = right.next, right_nxt
