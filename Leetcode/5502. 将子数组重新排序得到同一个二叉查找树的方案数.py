# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-30 16:27
 @Author  : QDY
 @FileName: 5502. 将子数组重新排序得到同一个二叉查找树的方案数.py
 @Software: PyCharm
"""
"""
给你一个数组 nums表示 1到 n的一个排列。我们按照元素在 nums中的顺序依次插入一个初始为空的二叉查找树（BST）。
请你统计将 nums重新排序后，统计满足如下条件的方案数：
重排后得到的二叉查找树与 nums原本数字顺序得到的二叉查找树相同。

比方说，给你nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。
数组[2,3,1]也能得到相同的 BST，但[3,2,1]会得到一棵不同的BST 。

请你返回重排 nums后，与原数组 nums得到相同二叉查找树的方案数。
由于答案可能会很大，请将结果对10^9 + 7取余数。


示例 1：
输入：nums = [2,1,3]
输出：1
解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。

示例 2：
输入：nums = [3,4,5,1,2]
输出：5
解释：下面 5 个数组会得到相同的 BST：
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

示例 3：
输入：nums = [1,2,3]
输出：0
解释：没有别的排列顺序能得到相同的 BST 。

示例 4：
输入：nums = [3,1,2,5,4,6]
输出：19

示例 5：
输入：nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
输出：216212978
解释：得到相同 BST 的方案数是 3216212999。将它对 10^9 + 7 取余后得到 216212978。

提示：
1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
nums中所有数 互不相同。

"""

import math


class Solution:
    def numOfWays(self, nums) -> int:
        def c(r, n):  # 计算组合数
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        def helper(nums):  # 计算有多少种方案
            n = len(nums)
            if n <= 1: return 1
            root = nums[0]  # 组成的BST要以nums[0]为根节点，也就是nums[0]一定放在第一个位置
            left, right = [], []
            for i in range(1, n):  # 将之后的数分为左右子树
                if nums[i] < root:
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            # 只要子树中数字的排列顺序不变，那么就能构成同一个BST
            l_num = helper(left)  # 分别计算左右子树各自有多少种保持BST不变的方案
            r_num = helper(right)
            # 剩余的n-1个位置中，选择len(left)个位置放入左子树的数，剩余放入右子树
            # 即求组合数C(len(left),n-1)
            # 每一种组合方法有l_num*r_num种方案
            return c(len(left), n - 1) * l_num * r_num

        res = helper(nums) - 1
        return res % (10 ** 9 + 7)
