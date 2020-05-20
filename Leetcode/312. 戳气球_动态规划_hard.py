# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/20 10:47
 @Author  : QDY
 @FileName: 312. 戳气球_动态规划_hard.py

    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

    现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

    求所能获得硬币的最大数量。

    说明:
    你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    示例:

    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""


class Solution:
    def maxCoins(self, nums):

        #  动态规划
        nums.append(1)  # 先在首尾两端加上边界
        nums.insert(0, 1)
        # dp[i][j]表示编号在(i,j)区间内的气球能获得的最大硬币值
        # 当i>=j-1时，dp[i][j] = 0
        # 在(i,j)内的气球中，设最后戳破第k个，则
        # dp[i][j] = max(dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])

        n = len(nums)
        dp = [[0] * n for i in range(n - 1)]
        for i in range(n - 3, -1, -1):  # 从下往上
            for j in range(i + 2, n):  # 从左往右
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][-1]
