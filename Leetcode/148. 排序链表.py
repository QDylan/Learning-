# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/6 23:50
 @Author  : QDY
 @FileName: 148. 排序链表.py

    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

    示例 1:

    输入: 4->2->1->3
    输出: 1->2->3->4
    示例 2:

    输入: -1->5->3->4->0
    输出: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        # 通过递归实现链表归并排序，有以下两个环节：

        # 分割 cut 环节： 找到当前链表中点，并从中点将链表断开（以便在下次递归 cut 时，链表片段拥有正确边界）；
        # 我们使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
        # 找到中点 slow 后，执行 slow.next = None 将链表切断。
        # 递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp(因为链表是从 slow 切断的)。
        # cut 递归终止条件： 当head.next == None时，说明只有一个节点了，直接返回此节点。
        # 合并 merge 环节： 将两个排序链表合并，转化为一个排序链表。
        # 双指针法合并，建立辅助ListNode h 作为头部。
        # 设置两指针 left, right 分别指向两链表头部，
        # 比较两指针处节点值大小，由小到大加入合并链表头部，指针交替前进，直至添加完两个链表。
        # 返回辅助ListNode h 作为头部的下个节点 h.next。
        # 时间复杂度 O(l + r)，l, r 分别代表两个链表长度。
        # 当题目输入的 head == None 时，直接返回None。
        if not head or not head.next: return head
        # fast,slow = head.next,head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # mid,slow.next = slow.next,None
        # # 拆分
        # left = self.sortList(head)
        # right = self.sortList(mid)
        # # 合并
        # cur = root = ListNode(None)
        # while left or right:
        #     if not left or (right and left.val>right.val):
        #         cur.next = ListNode(right.val)
        #         right = right.next
        #     else:
        #         cur.next = ListNode(left.val)
        #         left = left.next
        #     cur = cur.next
        # return root.next
        # 模拟上述的多轮排序合并：
        # 统计链表长度length，用于通过判断intv < length判定是否完成排序；
        # 额外声明一个节点res，作为头部后面接整个链表，用于：
        # intv *= 2即切换到下一轮合并时，可通过res.next找到链表头部h；
        # 执行排序合并时，需要一个辅助节点作为头部，而res则作为链表头部排序合并时的辅助头部pre；
        # 后面的合并排序可以将上次合并排序的尾部tail用做辅助节点。
        # 在每轮intv下的合并流程：
        # 根据intv找到合并单元1和单元2的头部h1, h2。由于链表长度可能不是2^n，需要考虑边界条件：
        # 在找h2过程中，如果链表剩余元素个数少于intv，则无需合并环节，直接break，执行下一轮合并；
        # 若h2存在，但以h2为头部的剩余元素个数少于intv，也执行合并环节，h2单元的长度为c2 = intv - i。
        # 合并长度为c1, c2的h1, h2链表，其中：
        # 合并完后，需要修改新的合并单元的尾部pre指针指向下一个合并单元头部h。
        # （在寻找h1, h2环节中，h指针已经被移动到下一个单元头部）
        # 合并单元尾部同时也作为下次合并的辅助头部pre。
        # 当h == None，代表此轮intv合并完成，跳出。
        # 每轮合并完成后将单元长度×2，切换到下轮合并：intv *= 2。
        length, cur = 0, head
        while cur:
            length += 1
            cur = cur.next
        root = ListNode(None)
        root.next = head
        part = 1
        while part < length:
            prev, cur = root, root.next
            while cur:  # 根据part寻找要合并的单元1和单元2的头部
                h1, i = cur, 0
                while i < part and cur:  # 找到单元1的结尾=单元2的开头
                    i += 1
                    cur = cur.next
                if i < part:  # 单元1长度不足part，不用合并直接跳出
                    break
                h2, i = cur, 0
                while i < part and cur:  # cur移动到下一组单元1的开头
                    i += 1
                    cur = cur.next
                l1, l2 = part, i  # 单元1和单元2的长度
                while l1 or l2:
                    if l2 == 0 or (l1 and h1.val < h2.val):
                        prev.next = h1
                        h1 = h1.next
                        l1 -= 1
                    else:
                        prev.next = h2
                        h2 = h2.next
                        l2 -= 1
                    prev = prev.next
                prev.next = cur
            part *= 2
        return root.next
