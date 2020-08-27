# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/27 10:36
 @Author  : QDY
 @FileName: 538. 把二叉搜索树转换为累加树.py
 @Software: PyCharm
"""
"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.val = 0

    def convertBST(self, root):
        if not root: return
        # cur,stack,val = root,[],0
        # while cur or stack:  # 反中序遍历 右->根->左
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.right
        #     else:
        #         cur = stack.pop()
        #         cur.val += val
        #         val = cur.val
        #         cur = cur.left
        # return root
        self.convertBST(root.right)  # 递归
        root.val += self.val
        self.val = root.val
        self.convertBST(root.left)
        return root
