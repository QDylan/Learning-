# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-29 9:57
 @Author  : QDY
 @FileName: 515. 在每个树行中找最大值.py
 @Software: PyCharm
"""
"""
您需要在二叉树的每一行中找到最大的值。

示例：
输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root):
        if not root: return []
        res, q = [], deque([root])
        while q:
            val = -float('inf')
            length = len(q)
            for i in range(length):
                node = q.popleft()
                val = max(val, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(val)
        return res
