# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-02 10:01
 @Author  : QDY
 @FileName: 590. N叉树的后序遍历.py
 @Software: PyCharm
"""
"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个3叉树:

返回其后序遍历: [5,6,3,2,4,1].

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
    def postorder(self, root):
        if not root: return []
        res, stack = [], [root]
        while stack:  # 根->右->左
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)
        return res[::-1]
