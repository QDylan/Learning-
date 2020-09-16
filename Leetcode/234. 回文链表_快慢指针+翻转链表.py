# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/8 15:44
 @Author  : QDY
 @FileName: 234. 回文链表_快慢指针+翻转链表.py

    请判断一个链表是否为回文链表。

    示例 1:
    输入: 1->2
    输出: false

    示例 2:
    输入: 1->2->2->1
    输出: true
    进阶：
    你能否用O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:  # O(n) 时间复杂度 O(1) 空间复杂度
    def isPalindrome(self, head):
        if not head or not head.next: return True
        slow, fast = head, head  # 快慢指针
        res = True
        while fast and fast.next:  #
            slow = slow.next
            fast = fast.next.next

        if fast:  # fast没指向None,表示链表长度为偶数
            slow = slow.next  # 慢指针再进一步

        prev, cur = slow, slow.next
        prev.next = None
        while cur:  # 将slow之后的链表翻转
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        start1, start2 = head, prev
        while start2:  # 从链的两端向中间遍历
            if start1.val != start2.val:
                res = False
                break
            start1, start2 = start1.next, start2.next
        # # 为了不破坏链表结构，可以利用prev将链表复原
        # cur = prev.next
        # prev.next = None
        # while cur:
        #     next_node = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_node
        # print(head)
        return res
