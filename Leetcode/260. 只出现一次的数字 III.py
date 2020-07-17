# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/17 10:01
 @Author  : QDY
 @FileName: 260. 只出现一次的数字 III.py

    给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

    示例 :
    输入: [1,2,1,3,2,5]
    输出: [3,5]

"""


class Solution:
    def singleNumber(self, nums):
        bitmask = 0
        for i in nums:
            bitmask ^= i
        # bitmask中为1的位置在nums中出现了奇数次
        diff = bitmask & -bitmask  # diff记录最右边的1
        # diff一定是一个无重复元素的一位，因为它在nums中只出现了奇数次
        x = 0
        for i in nums:
            if i & diff:  # 找出在diff位置上为1的元素，重复出现的元素被抵消
                x ^= i
        return [x, x ^ bitmask]
