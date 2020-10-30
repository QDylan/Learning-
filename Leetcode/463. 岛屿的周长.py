# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-30 10:01
 @Author  : QDY
 @FileName: 463. 岛屿的周长.py
 @Software: PyCharm
"""
"""
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。


示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：
"""


class Solution:
    def islandPerimeter(self, grid) -> int:
        res = 0
        h, w = len(grid), len(grid[0])
        for i in range(h):  # 直接遍历数组，只要前面有相邻的方格，就-2
            for j in range(w):
                if grid[i][j]:
                    res += 4
                    if i > 0 and grid[i - 1][j]: res -= 2
                    if j > 0 and grid[i][j - 1]: res -= 2
        return res
