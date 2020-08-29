# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-29 20:23
 @Author  : QDY
 @FileName: 494. 目标和.py
 @Software: PyCharm
"""
"""
    给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。
    现在你有两个符号+和-。对于数组中的任意一个整数，你都可以从+或-中选择一个符号添加在前面。
    返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
    
    示例：
    输入：nums: [1, 1, 1, 1, 1], S: 3
    输出：5
    解释：
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

    一共有5种方法让最终目标和为3。
    
    提示：
    数组非空，且长度不会超过 20 。
    初始的数组的和不会超过 1000 。
    保证返回的最终结果能被 32 位整数存下。

"""


class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        # 找到两个子集n1,n2使得sum(n1)-sum(n2)==S
        # sum(n1)-sum(n2)+sum(n1)+sum(n2)==S+sum(n1)+sum(n2)
        # 2sum(n1) = S+sum(nums)
        # sum(n1) = [S+sum(nums)]//2
        # 转换为子集背包问题： 找到子集n1使得sum(n1) = [S+sum(nums)]//2
        sum_ = sum(nums)
        if sum_ < S or S + sum_ & 1: return 0
        target = (S + sum_) // 2
        length = len(nums)
        dp = [0] * (target + 1)  # dp[i]=和为i的子集数量
        dp[0] = 1
        for n in nums:  # 计算选择前x个能组成多少个和为target的子集
            for i in range(target, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[target]
