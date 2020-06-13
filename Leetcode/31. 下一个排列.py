# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/13 11:48
 @Author  : QDY
 @FileName: 31. 下一个排列.py

    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。

    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        right = length - 1
        while right > 0 and nums[right - 1] >= nums[right]:  # 从右往左扫描
            right -= 1  # 左侧大于等于右侧，继续移动

        if right == 0:  # 说明整个序列是逆序的，无更大的排列
            nums[0:] = nums[::-1]
        else:  # nums[right:]是逆序的，无更大的排列
            for i in range(length - 1, right - 1, -1):  # 在nums[right:]中找出比nums[right-1]大的最右侧元素
                if nums[i] > nums[right - 1]: break
            # print(right,i)
            nums[right - 1], nums[i] = nums[i], nums[right - 1]  # 交换，交换完后nums[right:]仍是逆序的
            nums[right:] = nums[right:][::-1]  # 翻转nums[right:]
