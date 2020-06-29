# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 9:13
 @Author  : QDY
 @FileName: 329. 矩阵中的最长递增路径_动态规划+DFS.py

    给定一个整数矩阵，找出最长递增路径的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

    示例 1:
    输入: nums =
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    输出: 4
    解释: 最长递增路径为 [1, 2, 6, 9]。

    示例 2:
    输入: nums =
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
    输出: 4
    解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

"""


class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        height, width = len(matrix), len(matrix[0])
        self.res = 0
        visited = [[0] * width for i in range(height)]  # visited[i][j]记录以matrix[i][j]为起点的最大路径

        def dfs(x, y):
            visited[x][y] = 1
            if x > 0 and matrix[x - 1][y] > matrix[x][y]:
                if not visited[x - 1][y]:  # 若下一个可行点没有被访问过，则对其进行DFS
                    dfs(x - 1, y)
                visited[x][y] = max(visited[x][y], 1 + visited[x - 1][y])
            if x < height - 1 and matrix[x + 1][y] > matrix[x][y]:
                if not visited[x + 1][y]:
                    dfs(x + 1, y)
                visited[x][y] = max(visited[x][y], 1 + visited[x + 1][y])
            if y > 0 and matrix[x][y - 1] > matrix[x][y]:
                if not visited[x][y - 1]:
                    dfs(x, y - 1)
                visited[x][y] = max(visited[x][y], 1 + visited[x][y - 1])
            if y < width - 1 and matrix[x][y + 1] > matrix[x][y]:
                if not visited[x][y + 1]:
                    dfs(x, y + 1)
                visited[x][y] = max(visited[x][y], 1 + visited[x][y + 1])

            self.res = max(self.res, visited[x][y])

        for i in range(height):
            for j in range(width):
                if not visited[i][j]:
                    dfs(i, j)
                # print(visited)

        return self.res
