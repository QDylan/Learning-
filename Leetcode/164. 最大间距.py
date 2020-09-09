# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-09 16:59
 @Author  : QDY
 @FileName: 164. 最大间距.py
 @Software: PyCharm
"""
"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
如果数组元素个数小于 2，则返回 0。

示例1:
输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

示例2:
输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。

说明:
你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

"""

import math
class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n <= 1: return 0
        # nums.sort()
        # res = 0
        # for i in range(1,n):
        #     res =  max(res,nums[i]-nums[i-1])
        # return res

        # 桶排序
        max_, min_ = max(nums), min(nums)
        if n == 2: return max_ - min_
        if min_ == max_: return 0
        gap = math.ceil((max_ - min_) / (n - 1))  # 分成n-1个桶,每个桶大小为gap
        bucket_min = [float('inf')] * (n - 1)  # 只记录每个桶中最大的数和最小的数
        bucket_max = [-float('inf')] * (n - 1)
        for i in range(n):
            if nums[i] == max_:  # 特例
                bucket_min[-1] = min(bucket_min[-1], max_)
                continue
            # [min_,min_+gap),[min_+gap,min_+2*gap),...[min_+(n-2)*gap,min_+(n-1)*gap)
            index = (nums[i] - min_) // gap
            bucket_max[index] = max(nums[i], bucket_max[index])
            bucket_min[index] = min(nums[i], bucket_min[index])
        res = 0
        for i in range(n - 1):
            if bucket_max[i] != -float('inf'):
                prev_max = bucket_max[i]
                for j in range(i + 1, n - 1):
                    if bucket_min[j] != float('inf'):
                        res = max(res, bucket_min[j] - prev_max)
                        prev_max = bucket_max[j]
                break
        return res
