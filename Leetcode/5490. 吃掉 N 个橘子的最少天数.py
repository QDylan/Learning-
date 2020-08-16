# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/16 16:04
 @Author  : QDY
 @FileName: 5490. 吃掉 N 个橘子的最少天数.py
 @Software: PyCharm
"""
"""
    厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：
    吃掉一个橘子。
    如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
    如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
    每天你只能从以上 3 种方案中选择一种方案。
    请你返回吃掉所有 n 个橘子的最少天数。

    示例 1：
    输入：n = 10
    输出：4
    解释：你总共有 10 个橘子。
    第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
    第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
    第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
    第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
    你需要至少 4 天吃掉 10 个橘子。

    示例 2：
    输入：n = 6
    输出：3
    解释：你总共有 6 个橘子。
    第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
    第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
    第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
    你至少需要 3 天吃掉 6 个橘子。

    示例 3：
    输入：n = 1
    输出：1

    示例 4：
    输入：n = 56
    输出：6

    提示：
    1 <= n <= 2*10^9

"""
from functools import lru_cache


class Solution:

    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return 1 + min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3)

    # def minDays(self, n: int) -> int:
    #     @lru_cache(None)
    #     def helper(i):
    #         if i<=2:return i
    #         if i % 6 == 0:
    #             return min(helper(i//3),helper(i//2))+1
    #         elif i % 3 == 0:
    #             return min(helper(i-1),helper(i//3))+1
    #         elif i % 2 == 0:
    #             return min(helper(i-1),helper(i//2))+1
    #         else:
    #             return helper(i-1)+1

    #     return helper(n)
