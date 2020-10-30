# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-30 10:11
 @Author  : QDY
 @FileName: 653. 两数之和 IV - 输入 BST.py
 @Software: PyCharm
"""
"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root, k):
        visited = set()

        def dfs(root):
            if not root:
                return False
            if k - root.val in visited:
                return True
            visited.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
