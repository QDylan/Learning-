# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/6 9:42
 @Author  : QDY
 @FileName: 55. 跳跃游戏_贪心.py

    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。

    示例 1:
    输入: [2,3,1,1,4]
    输出: true
    解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

    示例 2:
    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""


class Solution:
    def canJump(self, nums):
        length = len(nums)
        if length <= 1: return True
        # 贪心算法，不断计算能跳跃到的最右位置
        # reachable = 0
        # for i in range(length):
        #     if i > reachable:
        #         return False
        #     if i+nums[i] >= length-1:
        #         return True
        #     reachable = max(i+nums[i], reachable)

        to_final = 1  # 记录需要跳跃几步到达的下一个点，可以保证跳到终点
        for i in range(length - 2, -1, -1):  # 从倒数第二个往前遍历
            if nums[i] >= to_final:  # 若i能跳跃到保证能跳到终点的下一个点
                to_final = 1  # 重置to_final
            else:  # 否则令to_final+1
                to_final += 1

        return to_final == 1  # i=0时，若nums[i]>=to_final,表示能跳到终点，会将to_final重置
