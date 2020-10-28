# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-28 11:11
 @Author  : QDY
 @FileName: 1631. 最小体力消耗路径.py
 @Software: PyCharm
"""
"""
你准备参加一场远足活动。给你一个二维rows x columns的地图heights，其中heights[row][col]表示格子(row, col)的高度。
一开始你在最左上角的格子(0, 0)，且你希望去最右下角的格子(rows-1, columns-1)（注意下标从 0 开始编号）。
你每次可以往 上，下，左，右四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值是路径上相邻格子之间 高度差绝对值的 最大值决定的。

请你返回从左上角走到右下角的最小体力消耗值。

示例 1：
输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路劲差值最大值为 3 。

示例 2：
输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。

示例 3：
输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。

提示：
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

"""
import heapq


class Solution:
    def minimumEffortPath(self, heights) -> int:
        h, w = len(heights), len(heights[0])
        M = h * w
        # Dijkstra
        visited = [False] * M
        mat = [float('inf')] * M
        mat[0] = 0
        heap = [(0, 0, 0, 0)]
        while heap:
            dd, x, y, idx = heapq.heappop(heap)  # 堆优化
            if idx == M - 1: return dd
            visited[idx] = True
            for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy
                nxt = nx * w + ny
                if nx < 0 or ny < 0 or nx == h or ny == w or visited[nxt]: continue
                nxt_dis = max(dd, abs(heights[x][y] - heights[nx][ny]))
                if nxt_dis < mat[nxt]:
                    mat[nxt] = nxt_dis
                    heapq.heappush(heap, (nxt_dis, nx, ny, nxt))
