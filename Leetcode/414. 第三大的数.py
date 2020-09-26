# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-26 19:50
 @Author  : QDY
 @FileName: 414. 第三大的数.py
 @Software: PyCharm
"""
"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:
输入: [2, 2, 3, 1]

输出: 1
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

"""


class Solution:
    def thirdMax(self, nums) -> int:
        max1 = max2 = max3 = -float('inf')
        for i in nums:
            if i in (max1, max2, max3): continue
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i
        return max1 if max3 == -float('inf') else max3
