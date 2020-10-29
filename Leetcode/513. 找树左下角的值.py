# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-29 9:48
 @Author  : QDY
 @FileName: 513. 找树左下角的值.py
 @Software: PyCharm
"""
"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:
输入:

    2
   / \
  1   3

输出:
1

示例 2:
输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7

注意: 您可以假设树（即给定的根节点）不为 NULL。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def findBottomLeftValue(self, root) -> int:
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
