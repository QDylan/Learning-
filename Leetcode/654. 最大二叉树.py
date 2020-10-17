# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-17 10:19
 @Author  : QDY
 @FileName: 654. 最大二叉树.py
 @Software: PyCharm
"""
"""
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

示例 ：
输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

提示：
给定的数组的大小在 [1, 1000] 之间。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums: return None
        val = max(nums)
        index = nums.index(val)
        root = TreeNode(val)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root
