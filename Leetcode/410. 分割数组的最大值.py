# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/16 10:04
 @Author  : QDY
 @FileName: 410. 分割数组的最大值.py


    给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

    注意:
    数组长度 n 满足以下条件:
    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)

    示例:
    输入:
    nums = [7,2,5,10,8]
    m = 2
    输出:
    18

    解释:
    一共有四种方法将nums分割为2个子数组。
    其中最好的方式是将其分为[7,2,5] 和 [10,8]，
    因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

"""


class Solution:
    def splitArray(self, nums, m):
        if m == 1: return sum(nums)
        n = len(nums)

        def feasible(guess):  # 判断是否存在划分使得m个子数组各自和的最大值<=guess
            tmp_sum, cnt = nums[0], 0
            for i in range(1, n):  # 计算要使每个划分的数组的和都不超过guess的划分数
                if tmp_sum + nums[i] <= guess:
                    tmp_sum += nums[i]
                else:
                    tmp_sum = nums[i]
                    cnt += 1
            return cnt <= m - 1  #

        left, right = max(nums), sum(nums)
        while left <= right:  # 二分搜索最小的guess
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
