# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/26 21:02
 @Author  : QDY
 @FileName: 142. 环形链表 II.py

    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    说明：不允许修改给定的链表。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):  # Floyd 算法

        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:  # 找到环，设环之前的链条的长度为a,环的长度为b,慢指针走了s步，则快指针走了2s步
                # 设快指针比慢指针走了x个环=多走b*x步,则s=b*x,说明此时慢指针走了整数倍环的长度
                fast = head  # 找环的入口：通过让快指针从头节点开始一步一步走，令慢指针再走a步
                while fast != slow:  # 此时慢指针走了a+b*x步，一定在环的入口处与快指针相遇
                    fast, slow = fast.next, slow.next
                return fast
        return
