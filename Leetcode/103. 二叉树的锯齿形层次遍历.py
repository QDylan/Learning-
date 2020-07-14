# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/14 8:28
 @Author  : QDY
 @FileName: 103. 二叉树的锯齿形层次遍历.py

    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
    例如：
    给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回锯齿形层次遍历如下：

    [
      [3],
      [20,9],
      [15,7]
    ]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue, res, mark = [root], [], False
        while queue:
            length = len(queue)
            tmp = []
            for i in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if mark:
                tmp.reverse()
                mark = False
            else:
                mark = True
            res.append(tmp)
        return res
