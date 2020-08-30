# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-30 16:08
 @Author  : QDY
 @FileName: 5500. 乘积为正数的最长子数组长度.py
 @Software: PyCharm
"""
"""
    给你一个整数数组 nums，请你求出乘积为正数的最长子数组的长度。
    一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
    请你返回乘积为正数的最长子数组长度。

    示例 1：
    输入：nums = [1,-2,-3,4]
    输出：4
    解释：数组本身乘积就是正数，值为 24 。

    示例 2：
    输入：nums = [0,1,-2,-3,-4]
    输出：3
    解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
    注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。

    示例 3：
    输入：nums = [-1,-2,-3,0,1]
    输出：2
    解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。

    示例 4：
    输入：nums = [-1,2]
    输出：1

    示例 5：
    输入：nums = [1,2,3,5,-6,4,0,10]
    输出：4
    
    提示：
    1 <= nums.length <= 10^5
    -10^9 <= nums[i]<= 10^9

"""


class Solution:
    def getMaxLen(self, nums) -> int:
        n = len(nums)
        res = 0
        # sgn,l = 1,-1  # 二次遍历
        # for i in range(n):
        #     if nums[i]==0:
        #         sgn, l = 1, i
        #         continue
        #     sgn *= (1 if nums[i]>0 else -1)
        #     if sgn>0:
        #         res = max(res,i-l)
        # sgn,r = 1,n
        # for i in range(n-1,-1,-1):
        #     if nums[i]==0:
        #         sgn, r = 1, i
        #         continue
        #     sgn *= (1 if nums[i]>0 else -1)
        #     if sgn>0:
        #         res = max(res,r-i)
        # return res
        first, sgn, length = None, 1, 0  # first记录第一个负数及之前有多少个数
        for i in range(n):
            if nums[i] == 0:  # 遇0重置
                first, sgn, length = None, 1, 0
                continue
            length += 1  # length为当前搜索长度
            if nums[i] < 0:
                sgn *= -1
                if first is None: first = length
            if sgn > 0:  #
                res = max(res, length)
            else:  # 去除第一个负数后可以使乘积为正
                res = max(res, length - first)
        return res
