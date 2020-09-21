# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-21 10:40
 @Author  : QDY
 @FileName: 1594. 矩阵的最大非负积.py
 @Software: PyCharm
"""
"""
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。
在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，
找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
返回 最大非负积 对 109+ 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。


示例 1：

输入：grid = [[-1,-2,-3],
            [-2,-3,-3],
            [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
示例 2：

输入：grid = [[1,-2,1],
            [1,-2,1],
            [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：

输入：grid = [[1, 3],
            [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
示例 4：

输入：grid = [[ 1, 4,4,0],
            [-2, 0,0,1],
            [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)

"""


class Solution:
    def maxProductPath(self, grid) -> int:

        h, w = len(grid), len(grid[0])
        mat = [[0] * w for _ in range(h)]
        mat[0][0] = [grid[0][0], grid[0][0]]
        for i in range(1, h):
            mat[i][0] = [grid[i][0] * mat[i - 1][0][0], grid[i][0] * mat[i - 1][0][0]]
        for j in range(1, w):
            mat[0][j] = [grid[0][j] * mat[0][j - 1][0], grid[0][j] * mat[0][j - 1][0]]
        # print(mat)
        for i in range(1, h):
            for j in range(1, w):
                val = [grid[i][j] * mat[i][j - 1][0], grid[i][j] * mat[i][j - 1][1], grid[i][j] * mat[i - 1][j][0],
                       grid[i][j] * mat[i - 1][j][1]]
                mat[i][j] = [max(val), min(val)]

        return -1 if mat[-1][-1][0] < 0 else mat[-1][-1][0] % (10 ** 9 + 7)
