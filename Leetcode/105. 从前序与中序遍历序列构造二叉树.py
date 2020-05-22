# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/22 9:24
 @Author  : QDY
 @FileName: 105. 从前序与中序遍历序列构造二叉树.py

    根据一棵树的前序遍历与中序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：

        3
       / \
      9  20
        /  \
       15   7

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder, p_start=0, p_end=None, i_start=0, i_end=None):
        if not preorder or not inorder: return None
        if p_end is None:
            p_end = len(preorder) - 1
            i_end = len(inorder) - 1

        if p_start > p_end: return None

        root = TreeNode(preorder[p_start])  # 先序遍历中的第一个节点为根节点
        mid = inorder.index(preorder[p_start])  # 获取root在中序遍历中的位置
        # 中序遍历inorder中以mid为分界点，i_start~mid-1为左子树的中序遍历，mid+1~i_end为右子树的中序遍历
        root.left = self.buildTree(preorder, inorder, p_start + 1, p_start + (mid - i_start), i_start, mid - 1)
        # 左子树的节点个数为mid-i_start
        # 先序遍历中第p_start+1~p_start+(mid-i_start)为左子树的先序遍历，p_start+(mid-i_start)+1~p_end为右子树
        root.right = self.buildTree(preorder, inorder, p_start + (mid - i_start) + 1, p_end, mid + 1, i_end)

        return root
