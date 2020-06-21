# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/21 8:58
 @Author  : QDY
 @FileName: 124. 二叉树中的最大路径和.py

    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。
    该路径至少包含一个节点，且不一定经过根节点。

    示例 1:

    输入: [1,2,3]

           1
          / \
         2   3

    输出: 6
    示例 2:

    输入: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    输出: 42

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        if not root: return
        res = -float('inf')

        def max_gain(node):  # 返回以node为根节点的子树能给其父节点路径贡献的最大和
            if not node: return 0

            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)

            tmp_res = left + right + node.val
            # 计算一次以node为根节点的maxPathSum
            nonlocal res
            res = max(res, tmp_res)

            return max(max(left, right) + node.val, 0)

        max_gain(root)
        return res
