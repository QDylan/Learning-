# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/6 10:35
 @Author  : QDY
 @FileName: 45. 跳跃游戏 II_贪心_hard.py

    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。

    示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

    说明:
    假设你总是可以到达数组的最后一个位置。

"""


class Solution:
    def jump(self, nums):
        end = len(nums)
        if end <= 2: return end - 1
        if nums[0] >= end - 1:
            return 1
        ## 动态规划 dp[i] = 跳到终点需要几步

        ## 贪心算法
        dp = [0] * end  # dp[i] = 到达i点最少需要多少步

        max_jump = 0  # 记录当前能跳到的最右位置
        for i in range(end - 1):  # 从起点开始遍历到倒数第二个点
            # print(dp)
            if nums[i] + i > max_jump:  # 只对能跳过超过当前最大跳跃位置的点处理
                if nums[i] + i >= end - 1:  # 若i能直接跳到终点，则返回
                    return dp[i] + 1
                for j in range(max_jump + 1, nums[i] + i + 1):  # 更新i在当前最大跳跃位置的dp[i]
                    dp[j] = dp[i] + 1
                max_jump = nums[i] + i
