# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/3 11:17
 @Author  : QDY
 @FileName: 1293. 网格中的最短路径.py
 @Software: PyCharm
"""
"""
    给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
    如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，
    并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

    示例 1：
    输入： 
    grid = 
    [[0,0,0],
     [1,1,0],
    [0,0,0],
     [0,1,1],
    [0,0,0]], 
    k = 1
    输出：6
    解释：
    不消除任何障碍的最短路径是 10。
    消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
     
    示例 2：
    输入：
    grid = 
    [[0,1,1],
     [1,1,1],
     [1,0,0]], 
    k = 1
    输出：-1
    解释：
    我们至少需要消除两个障碍才能找到这样的路径。
     
    提示：
    grid.length == m
    grid[0].length == n
    1 <= m, n <= 40
    1 <= k <= m*n
    grid[i][j] == 0 or 1
    grid[0][0] == grid[m-1][n-1] == 0

"""
from collections import deque


class Solution:
    def shortestPath(self, grid, k: int) -> int:
        h, w = len(grid), len(grid[0])
        # 从(0,0)到(h-1,w-1)最短只用h+w-2步，若k>=h+w-2,则一定可以以h+w-2步到达
        # 又因为grid[m-1][n-1] == 0,所以到终点的这一步一定不需要消除障碍物，
        # 故只需要k>=h+w-1即可
        if k >= h + w - 1 or (h == 1 and w == 1): return h + w - 2

        q = deque([(0, 0, k)])
        step = 1
        visited = set((0, 0, k))
        while q:
            length = len(q)
            for cnt in range(length):
                x, y, rest = q.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if nx == h - 1 and ny == w - 1:
                        return step
                    if 0 <= nx < h and 0 <= ny < w:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            visited.add((nx, ny, rest))
                            q.append((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            visited.add((nx, ny, rest - 1))
                            q.append((nx, ny, rest - 1))
            step += 1
        return -1
