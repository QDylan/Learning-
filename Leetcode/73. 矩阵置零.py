# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/23 10:46
 @Author  : QDY
 @FileName: 73. 矩阵置零.py
 @Software: PyCharm
"""
"""
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

    示例 1:
    输入: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

    示例 2:
    输入: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    输出: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    进阶:

    一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？

"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        h, w = len(matrix), len(matrix[0])
        col0 = False
        for i in range(h):
            if matrix[i][0] == 0:
                col0 = True  # 第一列是否要全置为0
            for j in range(1, w):  # 从第二列开始
                if matrix[i][j] == 0:  # (i,j)为0
                    matrix[0][j] = 0  # 第i行为0
                    matrix[i][0] = 0  # 第j列为0
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] != 0 and (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0  # 需要置为0的位置
        if matrix[0][0] == 0:  # 第一行是否要全置为0
            for j in range(w):
                matrix[0][j] = 0
        if col0:  # 第一列是否要全置为0
            for i in range(h):
                matrix[i][0] = 0
