# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/5 8:46
 @Author  : QDY
 @FileName: 面试题29. 顺时针打印矩阵.py

    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

    示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

    示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]
     

    限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

"""
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:return matrix
        height,width = len(matrix), len(matrix[0])
        i,j,res = 0,0,[]
        # 模拟过程
        while 0<=i<height and 0<=j<width and matrix[i][j] is not None:
            while j<width and matrix[i][j] is not None:  # 向右走
                res.append(matrix[i][j])
                matrix[i][j] = None  # 走过的地方标记为None
                j += 1
            j -= 1  # 超出边界，往左退一格
            i += 1

            while i<height and matrix[i][j] is not None:  # 向下走
                res.append(matrix[i][j])
                matrix[i][j] = None
                i += 1
            i -= 1
            j -= 1

            while j>=0 and matrix[i][j] is not None:  # 向左走
                res.append(matrix[i][j])
                matrix[i][j] = None
                j -= 1
            j += 1
            i -= 1

            while i>=0 and matrix[i][j] is not None:  # 向上走
                res.append(matrix[i][j])
                matrix[i][j] = None
                i -= 1
            i += 1
            j += 1

        return res