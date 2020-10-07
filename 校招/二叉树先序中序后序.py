# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-07 15:43
 @Author  : QDY
 @FileName: 二叉树先序中序后序.py
 @Software: PyCharm
"""
"""
分别按照二叉树先序，中序和后序打印所有的节点。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self, root):
        # write code here
        self.res = [[], [], []]

        def dfs(cur):
            if not cur: return
            self.res[0].append(cur.val)
            dfs(cur.left)
            self.res[1].append(cur.val)
            dfs(cur.right)
            self.res[2].append(cur.val)

        dfs(root)
        return self.res
