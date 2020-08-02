# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/2 10:22
 @Author  : QDY
 @FileName: 114. 二叉树展开为链表.py
 @Software: PyCharm
"""

"""
    给定一个二叉树，原地将它展开为一个单链表。
    
    例如，给定二叉树
    
        1
       / \
      2   5
     / \   \
    3   4   6
    将其展开为：
    
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 先序遍历
        # res, stack, cur = [], [], root
        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         res.append(cur.val)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop().right

        # cur = root
        # for val in res[1:]:
        #     cur.left = None
        #     cur.right = TreeNode(val)
        #     cur = cur.right

        if not root or (not root.left and not root.right): return

        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            cur = root.left
            if root.right:
                while cur.right:
                    cur = cur.right
                cur.right = root.right
            root.right = root.left
            root.left = None
