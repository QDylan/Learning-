# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/12 9:41
 @Author  : QDY
 @FileName: 18. 四数之和.py

    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
    使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    注意：
    答案中不可以包含重复的四元组。

    示例：
    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
    满足要求的四元组集合为：
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

"""


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                l, r = j + 1, length - 1  # 双指针
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < length and nums[l] == nums[l - 1]:
                            l += 1
                        while r > j and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[l] + nums[r] + nums[i] + nums[j] > target:
                        r -= 1
                    else:
                        l += 1
        return res
