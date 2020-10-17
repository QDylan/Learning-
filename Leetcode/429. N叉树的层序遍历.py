# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-17 10:26
 @Author  : QDY
 @FileName: 429. N叉树的层序遍历.py
 @Software: PyCharm
"""
"""
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个3叉树:

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]

说明:
树的深度不会超过1000。
树的节点总数不会超过5000。

"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque, defaultdict


class Solution:
    def levelOrder(self, root: 'Node'):
        if not root: return []
        # res = []
        # q = deque([root])
        # while q:
        #     cnt = len(q)
        #     tmp = []
        #     for i in range(cnt):
        #         node = q.popleft()
        #         tmp.append(node.val)
        #         for child in node.children:
        #             q.append(child)
        #     res.append(tmp)
        # return res
        res = defaultdict(list)

        def dfs(cur, depth):
            res[depth].append(cur.val)
            for child in cur.children:
                dfs(child, depth + 1)

        dfs(root, 0)
        return res.values()
