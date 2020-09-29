# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-29 10:49
 @Author  : QDY
 @FileName: 304. 二维区域和检索 - 矩阵不可变.py
 @Software: PyCharm
"""
"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1,col1) ，右下角为 (row2,col2)。
上图子矩阵左上角(row1, col1) = (2, 1)，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

说明:
你可以假设矩阵不可变。
会多次调用sumRegion方法。
你可以假设row1 ≤ row2 且col1 ≤ col2。

"""


class NumMatrix:

    def __init__(self, matrix):
        if not matrix: return
        h, w = len(matrix), len(matrix[0])
        self.grid = [[0] * (w + 1) for _ in range(h + 1)]  # 左边和上面多围一圈0,方便处理边界判断
        for i in range(h):
            for j in range(w):
                self.grid[i + 1][j + 1] = matrix[i][j] + self.grid[i][j + 1] + self.grid[i + 1][j] - self.grid[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2 + 1][col2 + 1] - self.grid[row1][col2 + 1] - self.grid[row2 + 1][col1] + self.grid[row1][
            col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
