# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/8 12:06
 @Author  : QDY
 @FileName: 645. 错误的集合.py

    集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，
    导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，
    再找到丢失的整数，将它们以数组的形式返回。

    示例 1:
    输入: nums = [1,2,2,4]
    输出: [2,3]

    注意:
    给定数组的长度范围是 [2, 10000]。
    给定的数组是无序的。

"""


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        # res = []
        # for i in range(n):  # 将abs(nums[i])-1作为索引，对应位置的元素置为负值
        #     id_ = abs(nums[i])-1
        #     if nums[id_] < 0:  # 若nums[id_]已经为负值了,则说明nums[i]已经出现过一次，nums[i]为重复元素
        #         dup = abs(nums[i])
        #     else:
        #         nums[id_] = -abs(nums[id_])
        # res.append(dup)

        # for i in range(n):  # 搜索nums中仍为正数的位置
        #     if nums[i] > 0:  # 若nums[i]为正数，说明其i+1不在原本的nums中
        #         res.append(i+1)  # 所以i+1为缺失元素
        #         break
        # return res

        # 数学方法
        S = sum(set(nums))
        res = [sum(nums) - S, n * (n + 1) // 2 - S]
        return res
