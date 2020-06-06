# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/6 11:38
 @Author  : QDY
 @FileName: 448. 找到所有数组中消失的数字.py

    给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。
    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗?
    你可以假定返回的数组不算在额外空间内。

    示例:
    输入:
    [4,3,2,7,8,2,3,1]
    输出:
    [5,6]

"""


class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        # 时间O(n) 空间O(1)实现 原地修改
        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
