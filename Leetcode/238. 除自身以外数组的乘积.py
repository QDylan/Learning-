# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/4 9:13
 @Author  : QDY
 @FileName: 238. 除自身以外数组的乘积.py

    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

    示例:
    输入: [1,2,3,4]
    输出: [24,12,8,6]
     

    提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

    进阶：
    你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

"""


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        if length <= 1: return nums
        output = [0] * length
        output[-1] = nums[-1]
        for i in range(length - 2, 0, -1):  # 从后往前累乘
            output[i] = output[i + 1] * nums[i]
        output[0] = output[1]  # output[0] = nums[1]*...*nums[length-1]

        tmp = nums[0]
        for i in range(1, length - 1):  # 从前往后累乘
            # tmp = nums[0]*...nums[i-1], output[i+1]= nums[i+1]*...nums[length-1]
            output[i] = tmp * output[i + 1]
            tmp *= nums[i]
        output[-1] = tmp  # output[length-1] = nums[0]*...num[length-2]

        return output
