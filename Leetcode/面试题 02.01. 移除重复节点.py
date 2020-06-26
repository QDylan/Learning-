# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/26 12:50
 @Author  : QDY
 @FileName: 面试题 02.01. 移除重复节点.py

    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

    示例1:
     输入：[1, 2, 3, 3, 2, 1]
     输出：[1, 2, 3]

    示例2:
     输入：[1, 1, 1, 1, 2]
     输出：[1, 2]

    提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。

    进阶：
    如果不得使用临时缓冲区，该怎么解决？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head):
        # 时间O(n),空间O(n)
        s = set()
        prev = ListNode(None)
        prev.next = head
        cur = head
        while cur:
            if not s.__contains__(cur.val):
                s.add(cur.val)
                prev.next = cur
                cur = cur.next
                prev = prev.next
            else:
                cur = cur.next
        prev.next = None
        return head

        # # 时间O(n^2), 空间O(1)
        # cur = head
        # while cur:
        #     prev = cur
        #     nxt = cur.next
        #     while nxt:
        #         if nxt.val == cur.val:
        #             prev.next = nxt.next
        #         else:
        #             prev = prev.next
        #         nxt = nxt.next
        #     cur = cur.next
        # return head
