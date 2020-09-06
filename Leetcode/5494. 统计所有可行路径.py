# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-06 17:14
 @Author  : QDY
 @FileName: 5494. 统计所有可行路径.py
 @Software: PyCharm
"""
"""
给你一个 互不相同的整数数组，其中locations[i]表示第i个城市的位置。
同时给你start，finish和fuel分别表示出发城市、目的地城市和你初始拥有的汽油总量

每一步中，如果你在城市 i，你可以选择任意一个城市 j，满足 j != i且0 <= j < locations.length，并移动到城市j。
从城市i移动到j消耗的汽油量为|locations[i] - locations[j]|，|x|表示x的绝对值。

请注意，fuel任何时刻都不能为负，且你可以经过任意城市超过一次（包括start和finish）。
请你返回从start到finish所有可能路径的数目。

由于答案可能很大， 请将它对10^9 + 7取余后返回。

示例 1：
输入：locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
输出：4
解释：以下为所有可能路径，每一条都用了 5 单位的汽油：
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3

示例 2：
输入：locations = [4,3,1], start = 1, finish = 0, fuel = 6
输出：5
解释：以下为所有可能的路径：
1 -> 0，使用汽油量为 fuel = 1
1 -> 2 -> 0，使用汽油量为 fuel = 5
1 -> 2 -> 1 -> 0，使用汽油量为 fuel = 5
1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 5

示例 3：
输入：locations = [5,2,1], start = 0, finish = 2, fuel = 3
输出：0
解释：没有办法只用 3 单位的汽油从 0 到达 2 。因为最短路径需要 4 单位的汽油。

示例 4 ：
输入：locations = [2,1,5], start = 0, finish = 0, fuel = 3
输出：2
解释：总共有两条可行路径，0 和 0 -> 1 -> 0 。

示例 5：
输入：locations = [1,2,3], start = 0, finish = 2, fuel = 40
输出：615088286
解释：路径总数为 2615088300 。将结果对 10^9 + 7 取余，得到 615088286 。


提示：
2 <= locations.length <= 100
1 <= locations[i] <= 10^9
所有locations中的整数 互不相同。
0 <= start, finish <locations.length
1 <= fuel <= 200

"""

from functools import lru_cache


class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        N = len(locations)

        # dp[end][f] = start到end点'正好'花费f的油的路径数
        @lru_cache(None)
        def helper(end, f):
            if f == 0:
                if end == start:
                    return 1
                else:
                    return 0
            dp = 0
            for i in range(N):
                if i == end: continue
                dd = abs(locations[i] - locations[end])
                if f >= dd:
                    dp += helper(i, f - dd)  # start到i正好花费f-dd的路径数
            return dp

        res = 0
        for f in range(fuel + 1):
            res += helper(finish, f)
        return res % mod
        # dp = [[0]*(fuel+1) for _ in range(N)]
        # dp[start][0] = 1
        # for f in range(fuel+1):
        #     for i in range(N):
        #         for j in range(N):
        #             if i==j:continue
        #             dd = abs(locations[i]-locations[j])
        #             if f>=dd:
        #                 dp[j][f] += dp[i][f-dd]
        # res = 0
        # for f in range(fuel+1):
        #     res += dp[finish][f]
        # return res % (10**9+7)
