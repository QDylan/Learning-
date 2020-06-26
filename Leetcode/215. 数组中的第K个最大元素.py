# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/26 13:42
 @Author  : QDY
 @FileName: 215. 数组中的第K个最大元素.py

    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

    示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

    说明:
    你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

"""
import random


class Solution:
    def findKthLargest(self, nums, k):

        def quick_sort(arr, first, last):
            if first >= last:
                if first == k - 1:
                    return arr[first]
                if last == k - 1:
                    return arr[last]
                return None

            index = random.randint(first, last)  # 取随机
            low, high, mid_val = first, last, nums[index]
            nums[low], nums[index] = nums[index], nums[low]
            while low < high:
                while low < high and arr[high] <= mid_val:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] > mid_val:
                    low += 1
                arr[high] = arr[low]

            if low == k - 1:
                return mid_val
            elif low > k - 1:
                return quick_sort(arr, first, low - 1)
            else:
                return quick_sort(arr, low + 1, last)

        return quick_sort(nums, 0, len(nums) - 1)
        # def merge_sort(arr):
        #     len_a = len(arr)
        #     if len_a<=1:return arr
        #     mid = len_a//2
        #     left = merge_sort(arr[:mid])
        #     right = merge_sort(arr[mid:])
        #     len_r = len_a-mid
        #     pos, l, r = 0, 0, 0
        #     while pos<len_a:
        #         if l==mid or (r<len_r and left[l]<=right[r]):
        #             arr[pos] = right[r]
        #             r += 1
        #         elif r==len_r or (l<mid and left[l]>right[r]):
        #             arr[pos] = left[l]
        #             l += 1
        #         pos += 1
        #     return arr
        # merge_sort(nums)
        # return nums[k-1]
