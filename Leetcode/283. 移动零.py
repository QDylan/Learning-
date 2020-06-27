# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/27 22:38
 @Author  : QDY
 @FileName: 283. 移动零.py

    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]

    说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lastnonzero = 0
        cur = 0
        while cur < n:
            if nums[cur] != 0:  # 找到非零数，移动到前面的最后一个非零数之后(最前面的0)
                nums[lastnonzero], nums[cur] = nums[cur], nums[lastnonzero]
                lastnonzero += 1  # 更新最后一个非零数的位置
            cur += 1
        # i = 0
        # while i<n:
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         i += 1
