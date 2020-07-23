# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/23 14:08
 @Author  : QDY
 @FileName: 74. 搜索二维矩阵.py
 @Software: PyCharm
"""
"""
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

    示例 1:
    输入:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    输出: true

    示例 2:
    输入:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 13
    输出: false

"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]: return False
        h, w = len(matrix), len(matrix[0])
        top, bottom = 0, h - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        top -= 1
        if top < 0:
            return False
        left, right = 0, w - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[top][mid] == target:
                return True
            if matrix[top][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        # i, j = 0, w-1
        # while i<h and j>=0:
        #     if matrix[i][j] == target:
        #         return True
        #     if matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return False
