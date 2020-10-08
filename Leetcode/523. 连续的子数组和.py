# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-08 11:08
 @Author  : QDY
 @FileName: 523. 连续的子数组和.py
 @Software: PyCharm
"""
"""
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

 

示例 1：

输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 

说明：

数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。

"""


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        length = len(nums)
        if length <= 1: return False
        if k == 0:
            for i in range(length - 1):
                if nums[i] == 0 and nums[i + 1] == 0: return True
            return False
        # x1+...+xi = n*k+a, x1+...+xj = m*k+a
        # -> x(i+1)+...+xj = (m-n)*k
        prefix, hm = 0, {0: -1}
        for i in range(length):
            prefix += nums[i]
            prefix %= k
            if prefix in hm and i - hm[prefix] > 1:  # 同余连续出现表示单个数整除k,不合题意
                return True
            elif prefix not in hm:  # 只记录最早出现的余数位置
                hm[prefix] = i
        return False
