# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/1 9:28
 @Author  : QDY
 @FileName: 153. 寻找旋转排序数组中的最小值.py

    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。

    示例 1:
    输入: [3,4,5,1,2]
    输出: 1

    示例 2:
    输入: [4,5,6,7,0,1,2]
    输出: 0

"""


class Solution:
    def findMin(self, nums):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[r] > nums[m]:  # 右边数组是有序的，最小值为nums[r]
                r = m  # 最小值（旋转点）在左边数组nums[l:m+1]中
            else:  # 右边数组是乱序的，最小值点（旋转点）在右边数组nums[m+1:r]中
                l = m + 1
        return nums[l]
