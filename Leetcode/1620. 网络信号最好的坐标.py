# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-20 10:24
 @Author  : QDY
 @FileName: 1620. 网络信号最好的坐标.py
 @Software: PyCharm
"""
"""
给你一个数组 towers和一个整数 radius，数组中包含一些网络信号塔，
其中towers[i] = [xi, yi, qi]表示第i个网络信号塔的坐标是(xi, yi)且信号强度参数为qi。
所有坐标都是在  X-Y 坐标系内的整数坐标。两个坐标之间的距离用 欧几里得距离计算。

整数radius表示一个塔 能到达的 最远距离。如果一个坐标跟塔的距离在 radius以内，那么该塔的信号可以到达该坐标。
在这个范围以外信号会很微弱，所以 radius以外的距离该塔是 不能到达的。

如果第 i个塔能到达 (x, y)，那么该塔在此处的信号为⌊qi / (1 + d)⌋，其中d是塔跟此坐标的距离。
一个坐标的 网络信号是所有 能到达该坐标的塔的信号强度之和。

请你返回 网络信号最大的整数坐标点。如果有多个坐标网络信号一样大，请你返回字典序最小的一个坐标。

注意：

坐标(x1, y1)字典序比另一个坐标(x2, y2)小：要么x1 < x2，要么x1 == x2 且y1 < y2。
⌊val⌋表示小于等于val的最大整数（向下取整函数）。

示例 1：
输入：towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出：[2,1]
解释：
坐标 (2, 1) 信号强度之和为 13
- 塔 (2, 1) 强度参数为 7 ，在该点强度为 ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- 塔 (1, 2) 强度参数为 5 ，在该点强度为 ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- 塔 (3, 1) 强度参数为 9 ，在该点强度为 ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
没有别的坐标有更大的信号强度。

示例 2：
输入：towers = [[23,11,21]], radius = 9
输出：[23,11]

示例 3：
输入：towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
输出：[1,2]

示例 4：
输入：towers = [[2,1,9],[0,1,9]], radius = 2
输出：[0,1]
解释：坐标 (0, 1) 和坐标 (2, 1) 都是强度最大的位置，但是 (0, 1) 字典序更小。

提示：
1 <= towers.length <= 50
towers[i].length == 3
0 <= xi, yi, qi <= 50
1 <= radius <= 50

"""


class Solution:
    def bestCoordinate(self, towers, radius: int):
        max_x, max_y, min_x, min_y = -float('inf'), -float('inf'), float('inf'), float('inf')
        for x, y, q in towers:
            max_x = max(x, max_x)
            min_x = min(x, min_x)
            max_y = max(y, max_y)
            min_y = min(y, min_y)

        def signal(i, j):
            ans = 0
            for x, y, q in towers:
                d = ((x - i) ** 2 + (y - j) ** 2) ** 0.5
                if d <= radius:
                    ans += int(q / (1 + d))
            return ans

        res, res_q = [], 0
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                tmp = signal(i, j)
                # print(i,j,tmp)
                if tmp > res_q:
                    res = [i, j]
                    res_q = tmp
        return res
