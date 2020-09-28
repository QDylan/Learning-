# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-28 11:12
 @Author  : QDY
 @FileName: 1091. 二进制矩阵中的最短路径.py
 @Software: PyCharm
"""
"""
在一个N ×N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格C_1, C_2, ..., C_k组成：

相邻单元格C_i 和C_{i+1}在八个方向之一上连通（此时，C_i 和C_{i+1}不同且共享边或角）
C_1 位于(0, 0)（即，值为grid[0][0]）
C_k位于(N-1, N-1)（即，值为grid[N-1][N-1]）
如果 C_i 位于(r, c)，则 grid[r][c]为空（即，grid[r][c] ==0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

示例 1：
输入：[[0,1],[1,0]]
输出：2

示例 2：
输入：[[0,0,0],[1,1,0],[1,1,0]]
输出：4

提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 为0 或1

"""
import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: return -1
        if n - 1 == 0: return 1

        def distance(x, y):
            return max(abs(n - 1 - x), abs(n - 1 - y))

        heap = [(distance(0, 0) + 1, 1, 0, 0)]
        while heap:  # A*搜索
            h, steps, x, y = heapq.heappop(heap)
            if grid[x][y] == 1: continue
            grid[x][y] = 1
            for nx, ny in (
            (x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1),
            (x + 1, y + 1)):
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    if nx == n - 1 and ny == n - 1: return steps + 1
                    heapq.heappush(heap, (distance(nx, ny) + steps, steps + 1, nx, ny))  # heuristic = distance+steps
        return -1
