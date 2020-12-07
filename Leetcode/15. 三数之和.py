# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/12 8:40
 @Author  : QDY
 @FileName: 15. 三数之和.py

    给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
    使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    示例：
    给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

"""
class Solution:
    def threeSum(self, nums):
        length = len(nums)
        nums.sort()  # 排序
        res = []
        for i in range(length-2):  # 在nums[i+1:]中寻找两个数
            if i>0 and nums[i] == nums[i-1]: continue  # 避免重复
            target = -nums[i]
            left = i+1  # 双指针
            right = length-1
            while left<right:
                if nums[left]+nums[right] == target:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while right>i and nums[right]==nums[right+1]:  # 避免重复
                        right -= 1
                    while left<length and nums[left]==nums[left-1]:
                        left += 1
                elif nums[left]+nums[right]>target:
                    right -= 1
                else:
                    left += 1
        return res