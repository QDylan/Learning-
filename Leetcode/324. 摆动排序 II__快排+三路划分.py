# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 13:37
 @Author  : QDY
 @FileName: 324. 摆动排序 II__快排+三路划分.py

    给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

    示例 1:
    输入: nums = [1, 5, 1, 1, 6, 4]
    输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
    示例 2:

    输入: nums = [1, 3, 2, 2, 3, 1]
    输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
    说明:
    你可以假设所有输入都会得到有效的结果。

    进阶:
    你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

"""


class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.找到n/2小的数
        # nums[:mid] 每个数都小于 nums[mid:]
        n = len(nums)
        if n <= 1: return nums
        mid = n // 2

        def quick_sort(arr, first, last):
            if first >= last:
                return
            low, high, mid_val = first, last, arr[first]
            while low < high:
                while low < high and arr[high] > mid_val:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] <= mid_val:
                    low += 1
                arr[high] = arr[low]
            arr[low] = mid_val
            if low == mid:
                return
            elif low < mid:
                quick_sort(arr, low + 1, last)
            else:
                quick_sort(arr, first, low - 1)

        quick_sort(nums, 0, n - 1)
        # nums.sort()
        # half = (n+1)//2
        # nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        # print(nums)
        # 三路划分，荷兰旗 虚拟索引做切分 i -> (2i+1)%(n|1)
        # 如果n为偶数，(n|1)为n+1，如果n为奇数，(n|1)仍为n
        mid_num = nums[mid]
        i, j, k = 0, 0, n - 1
        while j <= k:
            nxt_j = (2 * j + 1) % (n | 1)
            if nums[nxt_j] > mid_num:
                nxt_i = (2 * i + 1) % (n | 1)
                nums[nxt_i], nums[nxt_j] = nums[nxt_j], nums[nxt_i]
                i += 1
                j += 1
            elif nums[nxt_j] < mid_num:
                nxt_k = (2 * k + 1) % (n | 1)
                nums[nxt_j], nums[nxt_k] = nums[nxt_k], nums[nxt_j]
                k -= 1
            else:
                j += 1
            # print(nums,i,j,k)
