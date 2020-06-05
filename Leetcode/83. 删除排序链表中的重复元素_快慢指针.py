# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/5 11:18
 @Author  : QDY
 @FileName: 83. 删除排序链表中的重复元素_快慢指针.py

    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

    示例 1:

    输入: 1->1->2
    输出: 1->2
    示例 2:

    输入: 1->1->2->3->3
    输出: 1->2->3

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head: return head
        # prev,cur = head,head.next
        # while cur:
        #     if cur.val == prev.val:
        #         cur = cur.next
        #         prev.next = cur
        #     else:
        #         prev.next = cur
        #         prev = prev.next
        #         cur = cur.next

        # return head

        # 快慢指针
        slow, fast = head, head.next
        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        slow.next = None
        return head
