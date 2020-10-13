# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-13 12:59
 @Author  : QDY
 @FileName: 321. 拼接最大数.py
 @Software: PyCharm
"""
"""
给定长度分别为m和n的两个数组，其元素由0-9构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n)个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为k的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]

示例 3:
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

"""
from collections import deque


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0] * k

        def merge(A, B):  # 合并两组数组
            ans = []
            while A or B:
                if A > B:  # 取字典序较大的数组 [6,7]>[6,6,3];[1,2]<[1,2,3]
                    ans.append(A[0])
                    A.popleft()
                else:
                    ans.append(B[0])
                    B.popleft()
            return ans

        def pick(nums, i):  # 从nums中选出i个数字，使得数字排列最大
            stack = deque([])  # 维护一个单调递减的栈
            if i == 0: return stack
            cnt = len(nums) - i  # 相当于删去cnt个数字
            for j in nums:
                while stack and cnt > 0 and stack[-1] < j:
                    stack.pop()
                    cnt -= 1
                stack.append(j)
            while stack and cnt > 0:
                stack.pop()
                cnt -= 1
            return stack

        n1, n2 = len(nums1), len(nums2)
        for i in range(n1 + 1):
            j = k - i
            if j < 0: break
            if j > n2: continue
            # print(pick(nums1,i),i,pick(nums2,j),j,tmp)
            res = max(res, merge(pick(nums1, i), pick(nums2, j)))
        return res
