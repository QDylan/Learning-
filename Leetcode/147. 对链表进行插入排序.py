# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/15 11:16
 @Author  : QDY
 @FileName: 147. 对链表进行插入排序.py
 @Software: PyCharm
"""
"""
    插入排序算法：
    插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    重复直到所有输入数据插入完为止。
     
    示例 1：
    输入: 4->2->1->3
    输出: 1->2->3->4

    示例 2：
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next: return head
        head_ = ListNode(-float('inf'))
        head_.next = head
        prev, cur = head_, head
        while cur:
            if cur.val >= prev.val:  # 若比已排好序的序列的最大元素大，则不用处理
                cur, prev = cur.next, prev.next
            else:
                prev.next = cur.next  # 断链
                prev_ = head_
                while prev_.next.val <= cur.val:
                    prev_ = prev_.next
                prev_.next, cur.next = cur, prev_.next  # prev_.next.val > cur.val
                cur = prev.next
        return head_.next
