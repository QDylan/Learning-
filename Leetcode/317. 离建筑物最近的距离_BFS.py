# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/27 22:43
 @Author  : QDY
 @FileName: 317. 离建筑物最近的距离_BFS.py
 @Software: PyCharm
"""
"""
你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，
通过调研，你希望从它出发能在 最短的距离和 内抵达周边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。

提示：

你只能通过向上、下、左、右四个方向上移动。
给你一个由 0、1 和 2 组成的二维网格，其中：
0 代表你可以自由通过和选择建造的空地
1 代表你无法通行的建筑物
2 代表你无法通行的障碍物

示例：
输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
输出：7 
解析：
给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。

注意：
题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。

"""
from collections import deque


class Solution:
    def shortestDistance(self, grid) -> int:
        h, w = len(grid), len(grid[0])
        distance = [[[] for i in range(w)] for j in range(h)]
        buildings = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    buildings += 1
                    visited = set()
                    q = deque([(i, j)])
                    d = 0
                    while q:  # BFS
                        l = len(q)
                        for cnt in range(l):
                            x, y = q.popleft()
                            if d > 0: distance[x][y].append(d)
                            if x > 0 and grid[x - 1][y] == 0 and (x - 1, y) not in visited:
                                q.append((x - 1, y))
                                visited.add((x - 1, y))
                            if x < h - 1 and grid[x + 1][y] == 0 and (x + 1, y) not in visited:
                                q.append((x + 1, y))
                                visited.add((x + 1, y))
                            if y < w - 1 and grid[x][y + 1] == 0 and (x, y + 1) not in visited:
                                q.append((x, y + 1))
                                visited.add((x, y + 1))
                            if y > 0 and grid[x][y - 1] == 0 and (x, y - 1) not in visited:
                                q.append((x, y - 1))
                                visited.add((x, y - 1))
                        d += 1

        # print(buildings,distance)
        res = float('inf')
        for i in range(h):
            for j in range(w):
                if len(distance[i][j]) == buildings:
                    res = min(res, sum(distance[i][j]))
        return res if res != float('inf') else -1
