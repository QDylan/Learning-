# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-04 9:15
 @Author  : QDY
 @FileName: 257. 二叉树的所有路径.py
 @Software: PyCharm
"""
"""
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    说明:叶子节点是指没有子节点的节点。
    
    示例:
    输入:
    
       1
     /   \
    2     3
     \
      5
    
    输出: ["1->2->5", "1->3"]
    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root: return []
        if not root.left and not root.right:
            return ['%s' % root.val]
        res = []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for p in left:
            res.append('%s->%s' % (root.val, p))
        for p in right:
            res.append('%s->%s' % (root.val, p))
        return res
