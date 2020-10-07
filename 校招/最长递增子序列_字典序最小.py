# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-07 19:19
 @Author  : QDY
 @FileName: 最长递增子序列_字典序最小.py
 @Software: PyCharm
"""
"""
给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）
"""


#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
class Solution:
    def LIS(self, arr):
        # write code here
        if not arr: return []
        res, length, N = [arr[0]], 1, len(arr)
        max_len = [0] * N  # 记录以arr[i]结尾的最长递增子序列的末端id
        for i in range(1, N):
            l, r = 0, length
            while l < r:
                m = l + (r - l) // 2
                if res[m] < arr[i]:
                    l = m + 1
                else:
                    r = m
            max_len[i] = l
            if l == length:
                res.append(arr[i])
                length += 1
            else:
                res[l] = arr[i]
        j = length - 1
        for i in range(N - 1, -1, -1):  # 从后往前，贪心法找递增子序列中每个位置的元素
            if max_len[i] == j:  # max_len相同，位置靠后出现的元素较小，否则max_len会更大
                res[j] = arr[i]
                j -= 1
        return res
