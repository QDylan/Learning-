# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/24 9:53
 @Author  : QDY
 @FileName: 4. 寻找两个正序数组的中位数_二分查找_hard.py

    给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0

    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len2 > len1:  # 令nums1为较长的数组
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        mid = (len1 + len2 + 1)//2

        def find_Kth(nums1,start1,nums2,start2,k):  # 二分搜索找第k小的数

            if start1 >= len1:  # nums1已无可用位置
                return nums2[start2 + k - 1]  # 直接返回nums2从start2开始的第k个数
            if start2 >= len2:  # nums2已无可用位置
                return nums1[start1 + k - 1]  # 直接返回nums1从start1开始的第k个数
            if k == 1: # 若k=1,直接返回两数组最小的起点
                return min(nums1[start1], nums2[start2])
            # 在两个数组中分别作二分搜索（分别找出第k//2个数）
            id1 = start1 + k//2-1  # 在长度较大的数组上不会发生
            id2 = min(start2 + k//2-1, len2-1)  # 若nums2的第k//2个数超出了边界，则取其最后一个

            if nums1[id1] < nums2[id2]: # 若nums1的第k//2个数更小(从start1开始数)
                # 则说明真正第k小的数，应该在nums1[start1+k//2:]或者nums2[start2:start2+k//2+1]中
                # 前k//2小的数已经找到，在nums1[:start1+k//2]中
                # 继续在nums1[start1+k//2:]和nums2[start2:]中找第k-k//2小的数
                return find_Kth(nums1,start1+k//2,nums2,start2,k-k//2)
            else:  # 若nums2的第k//2个数超出了边界，则应找第k-(len(nums1)-start1)个数
                return find_Kth(nums1,start1,nums2,start2+k//2,k-(id2-start2+1))

        if (len1 + len2) % 2 == 0:
            return (find_Kth(nums1,0,nums2,0,mid)+find_Kth(nums1,0,nums2,0,mid+1))/2
        else:
            return find_Kth(nums1,0,nums2,0,mid)
