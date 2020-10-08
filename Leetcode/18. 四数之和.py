# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/12 9:41
 @Author  : QDY
 @FileName: 18. 四数之和.py

    给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，
    使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

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

from collections import defaultdict


class Solution:
    def fourSum(self, nums, target: int):
        res, N = [], len(nums)
        nums.sort()
        two_sum = defaultdict(list)  # 记录 两数之和：两数的id

        for j in range(N - 1, 2, -1):  # 从末尾到第4个数
            if j < N - 1 and nums[j] == nums[j + 1]:  # 剪枝，避免重复
                continue
            if 4 * nums[j] < target:  # 剪枝
                break
            if nums[j] + 3 * nums[0] > target:  # 剪枝
                continue
            for i in range(j - 1, 1, -1):
                if i < j - 1 and nums[i] == nums[i + 1]:
                    continue
                if nums[j] + 3 * nums[i] < target:
                    break
                if nums[j] + nums[i] + 2 * nums[0] > target:
                    continue
                two_sum[nums[i] + nums[j]].append((i, j))

        for i in range(N - 3):  # 从开头到倒数第4个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                continue
            for j in range(i + 1, N - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + 3 * nums[j] > target:
                    break
                if nums[i] + nums[j] + 2 * nums[-1] < target:
                    continue
                for ii, jj in two_sum[target - nums[i] - nums[j]]:
                    if j < ii:
                        res.append([nums[i], nums[j], nums[ii], nums[jj]])

        return res
# class Solution:
#     def fourSum(self, nums, target):
#         nums.sort()
#         length = len(nums)
#         res = []
#         for i in range(length - 3):
#             if i > 0 and nums[i] == nums[i - 1]: continue
#             for j in range(i + 1, length - 2):
#                 if j > i + 1 and nums[j] == nums[j - 1]: continue
#                 l, r = j + 1, length - 1  # 双指针
#                 while l < r:
#                     if nums[l] + nums[r] + nums[i] + nums[j] == target:
#                         res.append([nums[i], nums[j], nums[l], nums[r]])
#                         l += 1
#                         r -= 1
#                         while l < length and nums[l] == nums[l - 1]:
#                             l += 1
#                         while r > j and nums[r] == nums[r + 1]:
#                             r -= 1
#                     elif nums[l] + nums[r] + nums[i] + nums[j] > target:
#                         r -= 1
#                     else:
#                         l += 1
#         return res
