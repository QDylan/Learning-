# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/13 10:46
 @Author  : QDY
 @FileName: 19. 删除链表的倒数第N个节点.py

    给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

    示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
    给定的 n保证是有效的。

    进阶：
    你能尝试使用一趟扫描实现吗？

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # prehead = ListNode(None)
        # prehead.next = head
        # slow = prehead
        # fast =head
        # for i in range(n):
        #     fast = fast.next
        # while fast:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return prehead.next

        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:  # fast走到None,删除第一个节点
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
