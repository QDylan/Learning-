# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/6 11:13
 @Author  : QDY
 @FileName: 25. K 个一组翻转链表_hard.py

    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    示例：
    给你这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5

    说明：
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def len_k(self, head, k):  # 判断该链表长度是否大于等于k
        cur = head
        length = 0
        while cur and length < k:
            cur = cur.next
            length += 1
        return length == k

    def reverseKGroup(self, head, k):
        # 对于以head为头的链表,若其长度不足k,则不用翻转
        if not head or not self.len_k(head, k): return head

        prev, cur = head, head.next
        for i in range(k - 1):  # 1->2->3->4
            next_node = cur.next  # head=prev=1 cur=2 next_node = 3
            cur.next = prev  # 1<->2 3->4
            prev = cur  # prev = 2  # new_head
            cur = next_node  # cue = 3
            # prev指向新的头节点，cur指向下一个待交换的链表头
        head.next = self.reverseKGroup(cur, k)  # 递归 2->1->reverse_k(3->4)

        return prev
