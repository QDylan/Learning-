# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/4 22:56
 @Author  : QDY
 @FileName: 75. 颜色分类.py

    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

    注意:
    不能使用代码库中的排序函数来解决这道题。

    示例:
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]

    进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？

"""


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1  # l:最后一个0的右边界，r：第一个2的左边界
        i = 0
        while i <= r and l < r:  # 一次扫描，遇到0就放到前面，遇到2就放到后面
            if nums[i] == 0 and i > l:  # 遇到0，且i在l之后
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif i == l and nums[i] == 0:
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
