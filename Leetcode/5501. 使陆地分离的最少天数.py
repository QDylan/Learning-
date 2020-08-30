# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-30 18:53
 @Author  : QDY
 @FileName: 5501. 使陆地分离的最少天数.py
 @Software: PyCharm
"""
"""
给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。
岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
一天内，可以将任何单个陆地单元（1）更改为水单元（0）。
返回使陆地分离的最少天数。

示例 1：
输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
输出：2
解释：至少需要 2 天才能得到分离的陆地。
将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。

示例 2：
输入：grid = [[1,1]]
输出：2
解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
示例 3：
输入：grid = [[1,0,1,0]]
输出：0

示例 4：
输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,0,1,1]]
输出：1

示例 5：
输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,1,1,1]]
输出：2

提示：
1 <= grid.length, grid[i].length <= 30
grid[i][j] 为 0 或 1

"""


class Solution:
    def minDays(self, grid) -> int:  #
        h, w = len(grid), len(grid[0])
        low = {}  # low=visited 记录访问了的节点

        def dfs(x, y):
            if x < 0 or x == h or y < 0 or y == w or grid[x][y] == 0 or (x, y) in low:
                return
            low[(x, y)] = -1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        first = None
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1 and (i, j) not in low:
                    if first: return 0  # 有两块不连通的区域
                    first = (i, j)
                    dfs(i, j)

        if len(low) == 2: return 2  # 只有两个点

        self.weak = False  # 是否存在割点

        def tarjan(prev, cur, index):  # tarjan算法寻找割点
            if self.weak: return
            # low[node]记录node在子树中的最小的根
            dfn = low[cur] = index  # dfn记录访问到这个节点时的次序编号
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x = cur[0] + dx
                y = cur[1] + dy
                if (x, y) != prev and (x, y) in low:  # 找到下一个节点
                    if low[(x, y)] == -1:  # 未访问过
                        index += 1
                        tarjan(cur, (x, y), index)  # 访问下一个
                        if low[(x, y)] > dfn:  # 找到割点
                            # print((x,y))
                            self.weak = True
                            return
                    low[cur] = min(low[cur], low[(x, y)])

        tarjan((-1, -1), first, 0)
        print(low)
        return 1 if self.weak else 2
