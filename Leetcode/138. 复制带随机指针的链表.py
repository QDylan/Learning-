# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 20:27
 @Author  : QDY
 @FileName: 138. 复制带随机指针的链表.py

    给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

    要求返回这个链表的 深拷贝。 

    我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

    val：一个表示 Node.val 的整数。
    random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None
        cur = head
        hash_map = {}
        while cur:  # 第一遍遍历，将节点放入哈希表
            hash_map[cur] = Node(cur.val)
            cur = cur.next

        for cur in hash_map:  # 第二遍遍历，利用更新next和random
            if cur.next:
                hash_map[cur].next = hash_map[cur.next]
            if cur.random:
                hash_map[cur].random = hash_map[cur.random]
        return hash_map[head]
