# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/11 10:03
 @Author  : QDY
 @FileName: 1372. 二叉树中的最长交错路径.py

    给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

    选择二叉树中 任意 节点和一个方向（左或者右）。
    如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
    改变前进方向：左变右或者右变左。
    重复第二步和第三步，直到你在树中无法继续移动。
    交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

    请你返回给定树中最长 交错路径 的长度。

    示例 1：
    输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
    输出：3
    解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。

    示例 2：
    输入：root = [1,1,1,null,1,null,null,1,1,null,1]
    输出：4
    解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。

    示例 3：
    输入：root = [1]
    输出：0

    提示：
    每棵树最多有 50000 个节点。
    每个节点的值在 [1, 100] 之间。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root):
        if not root: return 0
        self.res = 0  # 全局变量记录最大交错路径长度

        # def dfs(node,direct):  # 深度优先遍历
        #     if not node:return 0
        #     if direct=='left':  # 下一个方向为left
        #         res1 = 1+dfs(node.left,'right')  # 以node.left为头，下一个方向为右（可以与node相连形成交错）
        #         res2 = dfs(node.left,'left')  # 以node.left为头，下一个方向为左
        #         self.res = max(self.res,res1,res2)
        #         return res1
        #     else:
        #         res1 = 1+dfs(node.right,'left')
        #         res2 = dfs(node.right,'right')
        #         self.res = max(self.res,res1,res2)
        #         return res1
        # res1 = dfs(root,'left')
        # res2 = dfs(root,'right')
        # self.res = max(self.res,res1,res2)
        # return self.res - 1
        def dfs(node, direct, length):
            if not node: return 0
            self.res = max(self.res, length)
            if direct:
                dfs(node.left, 0, length + 1)
                dfs(node.left, 1, 0)
            else:
                dfs(node.right, 1, length + 1)
                dfs(node.right, 0, 0)

        dfs(root, 1, 0)
        dfs(root, 0, 0)
        return self.res
