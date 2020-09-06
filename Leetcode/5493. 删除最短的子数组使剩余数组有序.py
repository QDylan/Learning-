# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-06 16:15
 @Author  : QDY
 @FileName: 5493. 删除最短的子数组使剩余数组有序.py
 @Software: PyCharm
"""
"""
给你一个整数数组 arr，请你删除一个子数组（可以为空），使得 arr中剩下的元素是 非递减 的。
一个子数组指的是原数组中连续的一个子序列。
请你返回满足题目要求的最短子数组的长度。

示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。

示例 2：
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。

示例 3：
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。

示例 4：
输入：arr = [1]
输出：0

提示：
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9

"""


class Solution:
    def findLengthOfShortestSubarray(self, nums) -> int:
        n = len(nums)
        if n <= 1: return 0
        end1 = -1
        for i in range(1, n):  # 寻找从头开始的最长有序部分
            if nums[i] < nums[i - 1]:
                end1 = i - 1
                break
        if end1 == -1: return 0  # 说明数组是有序的
        res = end1 + 1  # 记录有序部分的长度
        for i in range(n - 1, -1, -1):  # 计算从末尾往前的最长有序部分
            if end1 < 0 or nums[i] >= nums[end1]:  # nums[:end1+1] 可以与 nums[i:]组成有序数组
                res = max(res, end1 + 1 + n - i)
            else:
                while end1 >= 0 and nums[i] < nums[end1]:
                    end1 -= 1  # end1记录开头有序部分的数组的末尾位置
                res = max(res, end1 + 1 + n - i)  # 最终 nums[:end+1]可以与 nums[i:]组成有序数组
            if nums[i - 1] > nums[i]: break  # 不再是有序时中断
        return n - res
