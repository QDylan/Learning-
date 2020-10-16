# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-16 8:32
 @Author  : QDY
 @FileName: 977. 有序数组的平方.py
 @Software: PyCharm
"""
"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A已按非递减顺序排序。

"""


class Solution:
    def sortedSquares(self, A):
        # return sorted(map(lambda x:x**2,A))
        res, tmp = [], []
        for i in range(len(A)):
            if A[i] < 0:
                tmp.append(A[i] ** 2)
            else:
                break
        l, r = i - 1, i
        while l >= 0 or r < len(A):
            if r == len(A) or (l >= 0 and tmp[l] < A[r] ** 2):
                res.append(tmp[l])
                l -= 1
            else:
                res.append(A[r] ** 2)
                r += 1
        return res
