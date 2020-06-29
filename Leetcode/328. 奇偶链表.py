# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 23:03
 @Author  : QDY
 @FileName: 328. 奇偶链表.py

    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

    示例 1:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL

    示例 2:
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL

    说明:
    应当保持奇数节点和偶数节点的相对顺序。
    链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next: return head
        # 用变量 head 和 odd 保存奇链表的头和尾指针。 evenHead 和 even 保存偶链表的头和尾指针。
        # 算法会遍历原链表一次并把奇节点放到奇链表里去、偶节点放到偶链表里去
        odd, even, even_head = head, head.next, head.next
        while even and even.next:  # odd与even交叉，交叉之前的是已经排列好的两个链表
            odd.next = even.next  # 偶的下一个是奇数节点  不断地把奇数节点放到odd中
            odd = odd.next  # 移动奇数节点
            even.next = odd.next  # 把偶数节点放到even中
            even = even.next
        odd.next = even_head
        return head
