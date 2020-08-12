# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/12 21:21
 @Author  : QDY
 @FileName: 86. 分隔链表.py
 @Software: PyCharm
"""
"""
    给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
    你应当保留两个分区中每个节点的初始相对位置。
    
    示例:
    输入: head = 1->4->3->2->5->2, x = 3
    输出: 1->2->2->4->3->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        before, after = ListNode(None), ListNode(None)
        before_head, after_head = before, after
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next

        # new_head = ListNode(None)
        # new_head.next = head
        # slow = new_head
        # while slow.next and slow.next.val < x:
        #     slow = slow.next
        # prev, fast = slow, slow.next
        # while fast:
        #     if fast.val < x:
        #         prev.next = fast.next
        #         fast.next = slow.next
        #         slow.next = fast
        #         slow = slow.next
        #         fast = prev.next
        #     else:
        #         prev = prev.next
        #         fast = fast.next
        # return new_head.next
