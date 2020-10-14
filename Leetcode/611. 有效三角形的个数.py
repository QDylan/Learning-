# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-14 10:28
 @Author  : QDY
 @FileName: 611. 有效三角形的个数.py
 @Software: PyCharm
"""
"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:
输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

注意:
数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

"""


class Solution:
    def triangleNumber(self, nums) -> int:
        res, N = 0, len(nums)
        nums.sort()
        for i in range(N - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                # print(res,nums[i],nums[l],nums[r])
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
