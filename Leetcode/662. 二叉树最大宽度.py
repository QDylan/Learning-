# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-21 10:03
 @Author  : QDY
 @FileName: 662. 二叉树最大宽度.py
 @Software: PyCharm
"""
"""
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。
这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:
输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。

示例 2:
输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。

示例3:
输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。

示例 4:
输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
注意: 答案在32位有符号整数的表示范围内。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root: return 0
        res, left, cur_dep, q = 1, 0, 0, deque([(root, 0, 0)])
        while q:
            node, depth, pos = q.popleft()
            if node:
                q.append((node.left, depth + 1, pos * 2 + 1))
                q.append((node.right, depth + 1, pos * 2 + 2))
                if cur_dep != depth:
                    cur_dep += 1
                    left = pos
                res = max(res, pos - left + 1)
        return res
