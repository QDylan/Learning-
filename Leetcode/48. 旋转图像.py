# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 21:34
 @Author  : QDY
 @FileName: 48. 旋转图像.py

    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。

    说明：
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

    示例 1:
    给定 matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    原地旋转输入矩阵，使其变为:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

    示例 2:
    给定 matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ],
    原地旋转输入矩阵，使其变为:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]

"""


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return matrix
        n = len(matrix)
        if n == 1: return matrix
        # 先转置，再翻转
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

        # 单词循环中旋转4个点
        # l, r = 0, n-1
        # while l<r:
        #     for i in range(r-l):
        #         matrix[l+i][r],matrix[r][r-i],matrix[r-i][l],matrix[l][l+i] = matrix[l][l+i],matrix[l+i][r],matrix[r][r-i],matrix[r-i][l]
        #     l += 1
        #     r -= 1
