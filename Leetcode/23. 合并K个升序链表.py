# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-05 16:08
 @Author  : QDY
 @FileName: 23. 合并K个升序链表.py
 @Software: PyCharm
"""
"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if not lists: return
        length = len(lists)
        if length == 1: return lists[0]
        m = length // 2
        left = self.mergeKLists(lists[:m])
        right = self.mergeKLists(lists[m:])
        head = ListNode(None)
        cur = head
        while left and right:
            if right.val > left.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if not left:
            cur.next = right
        elif not right:
            cur.next = left
        return head.next
