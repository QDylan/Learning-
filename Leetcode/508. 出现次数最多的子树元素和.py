# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-17 10:16
 @Author  : QDY
 @FileName: 508. 出现次数最多的子树元素和.py
 @Software: PyCharm
"""
"""
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

示例 1：
输入:
  5
 /  \
2   -3
返回[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例2：
输入：
  5
 /  \
2   -5
返回[2]，只有 2 出现两次，-5 只出现 1 次。

提示：假设任意子树元素和均可以用 32 位有符号整数表示。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        if not root: return []
        self.sum = defaultdict(int)

        def traverse(node):
            left = traverse(node.left) if node.left else 0
            right = traverse(node.right) if node.right else 0
            s = node.val + left + right
            self.sum[s] += 1
            return s

        traverse(root)
        res, cnt = [], 0
        for s in self.sum:
            if self.sum[s] > cnt:
                res = [s]
                cnt = self.sum[s]
            elif self.sum[s] == cnt:
                res.append(s)
        return res
