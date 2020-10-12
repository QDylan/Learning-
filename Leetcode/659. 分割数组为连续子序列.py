# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-12 11:31
 @Author  : QDY
 @FileName: 659. 分割数组为连续子序列.py
 @Software: PyCharm
"""
"""
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5

示例 2：
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5

示例 3：
输入: [1,2,3,4,4,5]
输出: False

提示：
输入的数组长度范围为 [1, 10000]

"""
from collections import Counter


class Solution:
    def isPossible(self, nums) -> bool:  # 贪心
        count = Counter(nums)  # 记录nums中剩余的数字
        tails = Counter()  # 存储以数字x结尾的长度不小于3的连续子序列个数
        for x in nums:
            if count[x] == 0:  # x 已消耗完
                continue
            elif tails[x - 1] > 0:  # 以x结尾, 存在以x-1结尾的合法子序列，那么x可以接在其之后
                tails[x - 1] -= 1
                tails[x] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:  # 以x为首，可以找到一个合法的子序列
                count[x + 1] -= 1
                count[x + 2] -= 1
                tails[x + 2] += 1
            else:  # x无法向前或向后找到其所在的合法子序列
                return False
            count[x] -= 1
        return True
