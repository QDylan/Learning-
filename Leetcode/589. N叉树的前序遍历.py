# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-30 10:45
 @Author  : QDY
 @FileName: 589. N叉树的前序遍历.py
 @Software: PyCharm
"""
"""
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个3叉树:

返回其前序遍历: [1,3,5,6,2,4]。

说明:递归法很简单，你可以使用迭代法完成此题吗?

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root):
        if not root: return []
        self.res = []

        # def travel(node):
        #     self.res.append(node.val)
        #     for nxt in node.children:
        #         travel(nxt)
        # travel(root)
        # return self.res

        stack = [root]
        while stack:  # 迭代
            cur = stack.pop()
            self.res.append(cur.val)
            stack.extend(cur.children[::-1])

        return self.res
