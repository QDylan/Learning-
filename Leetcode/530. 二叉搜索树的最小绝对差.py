# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-12 10:29
 @Author  : QDY
 @FileName: 530. 二叉搜索树的最小绝对差.py
 @Software: PyCharm
"""
"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 
提示：
树中至少有 2 个节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        stack, cur, res, prev = [], root, float('inf'), -float('inf')
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res = min(cur.val - prev, res)
                prev = cur.val
                cur = cur.right
        return res
