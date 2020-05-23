# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/22 18:25
 @Author  : QDY
 @FileName: 198.213.337.打家劫舍I.II.III_动态规划.py
 @Software: PyCharm
"""


class Solution:
    """
    1. 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
    影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

    示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
       偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

    """

    def rob_1(self, nums):

        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        # 状态转移方程： dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        #         dp = []
        #         dp.append(nums[0])
        #         dp.append(max(nums[0], nums[1]))
        #         for i in range(2, length):
        #             dp.append(max(dp[i-1], dp[i-2]+nums[i]))

        #         return dp[length-1]
        x, y = 0, 0
        for i in range(length):
            z = max(x + nums[i], y)
            x, y = y, z

        return y

    '''2.这个个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的'''

    def rob_2(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]

        # 将环分成两个队列：1~n-1 and 2~n
        x, y = 0, 0
        for i in range(length - 1):
            z = max(x + nums[i], y)
            x, y = y, z

        x_, y_ = 0, 0
        for i in range(1, length):
            z_ = max(x_ + nums[i], y_)
            x_, y_ = y_, z_

        return max(y, y_)

    '''   
    3.在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
    除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
    如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
    输入: [3,4,5,1,3,null,1]

        3
       / \
      4   5
     / \   \
    1   3   1

    输出: 9

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    '''


def rob_3(self, root):
    if root is None:
        return 0

    def post_count(root):
        # 后序遍历计算
        if root.left is not None:
            self.post_count(root.left)

        if root.right is not None:
            self.post_count(root.right)

        unchoose = 0  # 不选择根节点
        choose = root.val  # 选择根节点

        if root.left is not None:
            unchoose += root.left.val
            if root.left.left is not None:
                choose += root.left.left.val
            if root.left.right is not None:
                choose += root.left.right.val

        if root.right is not None:
            unchoose += root.right.val
            if root.right.left is not None:
                choose += root.right.left.val
            if root.right.right is not None:
                choose += root.right.right.val

        root.val = max(unchoose, choose)

    post_count(root)
    return root.val
