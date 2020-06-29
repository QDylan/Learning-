# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 10:15
 @Author  : QDY
 @FileName: 179. 最大数.py

    给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

    示例 1:
    输入: [10,2]
    输出: 210

    示例 2:
    输入: [3,30,34,5,9]
    输出: 9534330
    说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

"""


class Solution:
    def largestNumber(self, nums) -> str:
        nums = [str(i) for i in nums]

        # 定义一种新的比较大小方法：a+b>b+a -> a>b
        def quick_sort(arr, first, last):
            if first >= last: return arr
            low, high, mid = first, last, arr[first]
            while low < high:
                while low < high and arr[high] + mid <= mid + arr[high]:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] + mid > mid + arr[low]:
                    low += 1
                arr[high] = arr[low]
            arr[low] = mid
            quick_sort(arr, first, low - 1)
            quick_sort(arr, low + 1, last)

        # quick_sort(nums,0,len(nums)-1)
        def merge_sort(nums):
            n = len(nums)
            if n <= 1: return nums
            mid = n // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            l, r, pos = 0, 0, 0
            while l < mid or r < n - mid:
                if r == n - mid or (l < mid and left[l] + right[r] >= right[r] + left[l]):
                    nums[pos] = left[l]
                    l += 1
                    pos += 1
                elif l == mid or (r < n - mid and left[l] + right[r] < right[r] + left[l]):
                    nums[pos] = right[r]
                    r += 1
                    pos += 1
            return nums

        nums = merge_sort(nums)

        return ''.join(nums) if nums[0] != '0' else '0'
