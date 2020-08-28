# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/28 9:43
 @Author  : QDY
 @FileName: 437. 路径总和 III.py
 @Software: PyCharm
"""
"""
    给定一个二叉树，它的每个结点都存放着一个整数值。
    找出路径和等于给定数值的路径总数。
    路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
    二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
    
    示例：
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    
    返回 3。和等于 8 的路径有:
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3.  -3 -> 11

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def pathSum(self, root, target: int) -> int:
        if not root:return 0
        def helper(node,prefix,target):
            res = 0
            nxt_prefix = {num+node.val:prefix[num] for num in prefix}
            if target in nxt_prefix:res += nxt_prefix[target]
            if 0 in nxt_prefix:nxt_prefix[0]+=1
            else:nxt_prefix[0]=1
            left = helper(node.left,nxt_prefix,target) if node.left else 0
            right = helper(node.right,nxt_prefix,target) if node.right else 0
            return left+right+res
        return helper(root,{0:1},target)