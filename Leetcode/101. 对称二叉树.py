# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/31 15:12
 @Author  : QDY
 @FileName: 101. 对称二叉树.py

    给定一个二叉树，检查它是否是镜像对称的。

    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3
     

    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def symmetric(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and self.symmetric(left.right, right.left) and self.symmetric(left.left, right.right)

    def isSymmetric(self, root):
        if not root:return True
        # return self.symmetric(root.left, root.right)  # 递归
        queue = [root, root]
        while queue:
            node_r = queue.pop()
            node_l = queue.pop()
            if not node_l and not node_r:
                continue
            elif not node_l or not node_r or node_l.val != node_r.val:
                return False
            queue.append(node_r.right)
            queue.append(node_l.left)
            queue.append(node_l.right)
            queue.append(node_r.left)

        return True