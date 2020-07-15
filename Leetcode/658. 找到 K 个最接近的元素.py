# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/15 16:12
 @Author  : QDY
 @FileName: 658. 找到 K 个最接近的元素.py

    给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。
    返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

    示例 1:
    输入: [1,2,3,4,5], k=4, x=3
    输出: [1,2,3,4]

    示例 2:
    输入: [1,2,3,4,5], k=4, x=-1
    输出: [1,2,3,4]
     
    说明:
    k 的值为正数，且总是小于给定排序数组的长度。
    数组不为空，且长度不超过 104
    数组里的每个元素与 x 的绝对值不超过 104

"""


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        n = len(arr)
        l, r = 0, n
        while l < r:  # 二分搜索x的边界l，l之前的都小于等于x,l之后的都大于x
            m = l + (r - l) // 2
            if arr[m] <= x:
                l = m + 1
            else:
                r = m
        while l > 0 and r < n and r - l < k:  # arr[l:r]为所选数组
            if x - arr[l - 1] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        if l == 0:
            return arr[:k]
        if r == n:
            return arr[n - k:]
        return arr[l:r]
