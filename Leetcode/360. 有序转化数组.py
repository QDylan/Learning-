# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/28 9:33
 @Author  : QDY
 @FileName: 360. 有序转化数组.py
 @Software: PyCharm
"""
"""
    给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，
    计算函数值 f(x) = ax2 + bx + c，请将函数值产生的数组返回。
    要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。

    示例 1：
    输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
    输出: [3,9,15,33]

    示例 2：
    输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
    输出: [-23,-5,1,7]

"""


class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        if not nums: return []

        def f(x):
            return a * (x ** 2) + b * x + c

        if a == 0:  # 若a=0,退化为1次函数
            return [b * x + c for x in nums] if b >= 0 else [b * x + c for x in nums][::-1]

        extremum = -b / (2 * a)  # 抛物线中点
        left, right = [], []
        for i in range(len(nums)):  # 找到extremum的分界索引i
            if nums[i] < extremum:  # 在查找过程中同时变换left数组的值
                nums[i] = f(nums[i])
            else:  # 将数组按extremmum分成两部分
                right = [f(x) for x in nums[i:]]
                break
        left = nums[:i]

        def merge(left, right):  # 合并两个有序数组
            if not left: return right
            if not right: return left
            l, r, res = 0, 0, []
            while l < len(left) or r < len(right):
                if r == len(right) or (l < len(left) and left[l] < right[r]):
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            return res

        if a > 0:  # 若a>0，则left将由单调递增变为单调递减
            return merge(left[::-1], right)
        else:
            return merge(left, right[::-1])
