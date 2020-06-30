# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/30 22:31
 @Author  : QDY
 @FileName: 81. 搜索旋转排序数组 II.py

    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

    示例 1:
    输入: nums = [2,5,6,0,0,1,2], target = 0
    输出: true

    示例 2:
    输入: nums = [2,5,6,0,0,1,2], target = 3
    输出: false

    进阶:

    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

"""


class Solution:
    def search(self, nums, target):

        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[m] == nums[l]:
                l += 1
                continue
            if nums[m] > nums[l]:  # 左边是有序的
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]:  # 右边是有序的
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
        return False
