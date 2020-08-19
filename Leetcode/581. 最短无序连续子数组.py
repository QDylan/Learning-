# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/19 10:36
 @Author  : QDY
 @FileName: 581. 最短无序连续子数组.py
 @Software: PyCharm
"""
"""
    给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

    你找到的子数组应是最短的，请输出它的长度。

    示例 1:
    输入: [2, 6, 4, 8, 10, 9, 15]
    输出: 5
    解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
    说明 :

    输入的数组长度范围在 [1, 10,000]。
    输入的数组可能包含重复元素 ，所以升序的意思是<=。

"""


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        if not nums: return 0
        max_val, length = nums[0], len(nums)
        left, right = 0, 0
        for i in range(1, length):  # 从左到右循环，记录最大值为 max，若 nums[i] < max, 则表明位置 i 需要调整
            if nums[i] < max_val:
                right = i
            else:
                max_val = nums[i]
        if right == 0: return 0  # 数组是升序的
        min_val = nums[-1]
        for i in range(length - 2, -1, -1):  # 从右到左循环，记录最小值为 min, 若 nums[i] > min, 则表明位置 i 需要调整
            if nums[i] > min_val:
                left = i
            else:
                min_val = nums[i]

        return right + 1 - left
