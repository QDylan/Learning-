# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 9:49
 @Author  : QDY
 @FileName: 334. 递增的三元子序列.py

    给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

    数学表达式如下:

    如果存在这样的i, j, k,且满足0 ≤ i < j < k ≤ n-1，
    使得arr[i] < arr[j] < arr[k] ，返回 true ;否则返回 false 。
    说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

    示例 1:
    输入: [1,2,3,4,5]
    输出: true

    示例 2:
    输入: [5,4,3,2,1]
    输出: false

"""


class Solution:
    def increasingTriplet(self, nums):  # 双指针的贪心算法 时间O(N),空间O(1)
        low, mid = float('inf'), float('inf')
        for n in nums:  # 从头扫描一次数组
            if n <= low:  # low记录遇到的最小值
                low = n
            elif n <= mid:  # mid记录比low大的最小值,mid指向的值有可能在low指向的值之前
                mid = n  # mid<float('inf') 表示在mid之前存在一个比mid还小的数
            else:  # 当遇到比mid大的数时，说明找到了3个递增的数
                return True
        return False
