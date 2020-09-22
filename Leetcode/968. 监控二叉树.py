# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-22 10:15
 @Author  : QDY
 @FileName: 968. 监控二叉树.py
 @Software: PyCharm
"""
"""
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
计算监控树的所有节点所需的最小摄像头数量。

示例 1：
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。

示例 2：
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：
给定树的节点数的范围是[1, 1000]。
每个节点的值都是 0。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root) -> int:
        if not root: return 0
        self.res = 0

        def helper(root):  # 返回 节点的三种状态：1.装了监控 2.没装监控，但可以被监控到 3.不能被监控到
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            if left == 3 or right == 3:  # root必须装监控
                self.res += 1
                return 1
            elif left == 1 or right == 1:  # root能被看到 可以不装监控，
                return 2
            else:  # left==2 and right==2, root暂时不能被，可以不装监控，要求父节点装监控
                return 3

        if helper(root) == 3: self.res += 1
        return self.res
