# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 17:17
 @Author  : QDY
 @FileName: 199. 二叉树的右视图.py

    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    示例:

    输入: [1,2,3,null,5,null,4]
    输出: [1, 3, 4]
    解释:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        # 1.层次遍历
        res, queue = [], [root]
        while queue:
            res.append(queue[-1].val)
            # length = len(queue)
            # for i in range(length):
            #     node = queue.pop(0)
            #     if node.left:
            #         queue.append(node.left)
            #     if node.right:
            #         queue.append(node.right)
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res

        # # 2.
        # res = [root.val]
        # right = self.rightSideView(root.right)
        # left = self.rightSideView(root.left)
        # res += right
        # if len(left)>len(right):
        #     for i in range(len(right),len(left)):
        #         res.append(left[i])  # 添加左树长于右树的部分
        # return res
