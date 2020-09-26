# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-26 19:45
 @Author  : QDY
 @FileName: 628. 三个数的最大乘积.py
 @Software: PyCharm
"""
"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

"""


class Solution:
    def maximumProduct(self, nums) -> int:
        # nums.sort()
        # return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for i in nums:
            if i < min1:
                min1, min2 = i, min1
            elif i < min2:
                min2 = i
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i
        return max(max1 * max2 * max3, max1 * min1 * min2)
