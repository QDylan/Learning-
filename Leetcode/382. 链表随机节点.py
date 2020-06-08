# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/8 16:58
 @Author  : QDY
 @FileName: 382. 链表随机节点.py

    给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

    进阶:
    如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

    示例:

    // 初始化一个单链表 [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);

    // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
    solution.getRandom();

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        """
        if not self.head:return None
        cur = self.head.next
        res = self.head.val
        i = 2
        while cur:  # 当你遇到第 i 个元素时，有1/i的概率选择该元素，1-1/i的概率保持原有的选择
            if random.randint(1, i) == 1:  # 在[1,i]中随机取一个整数为1的概率=1/i
                res = cur.val  # 最后返回第i个元素的概率=1/i*i/(i+1)*(i+1)/(i+2)*...*(n-1)/n=1/n
            cur = cur.next
            i += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()