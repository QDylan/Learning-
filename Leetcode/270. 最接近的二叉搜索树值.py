# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/21 10:08
 @Author  : QDY
 @FileName: 270. 最接近的二叉搜索树值.py

    给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

    注意：

    给定的目标值 target 是一个浮点数
    题目保证在该二叉搜索树中只会存在一个最接近目标值的数
    示例：

    输入: root = [4,2,5,1,3]，目标值 target = 3.714286

        4
       / \
      2   5
     / \
    1   3

    输出: 4

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        if root.val == target:
            return root.val
        if root.left or root.right:
            if root.val > target:  # 根节点>目标值，更接近的值应该到左子树中搜索
                if not root.left:  # 若无左子树，则直接返回根节点的值
                    return root.val
                else:  # 比较左子树中最接近的值与根节点哪个更接近target
                    tmp = self.closestValue(root.left, target)
                    return root.val if root.val - target < abs(tmp - target) else tmp
            else:  # 根节点<目标值，更接近的值应该到右子树中搜索
                if not root.right:
                    return root.val
                else:
                    tmp = self.closestValue(root.right, target)
                    return root.val if target - root.val < abs(tmp - target) else tmp
        return root.val