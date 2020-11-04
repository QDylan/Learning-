# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-04 10:40
 @Author  : QDY
 @FileName: 397. 整数替换.py
 @Software: PyCharm
"""
"""
给定一个正整数n ，你可以做如下操作：

如果n是偶数，则用n / 2替换n 。
如果n是奇数，则可以用n + 1或n - 1替换n 。
n变为 1 所需的最小替换次数是多少？

示例 1：
输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1

示例 2：
输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1

示例 3：
输入：n = 4
输出：2

提示：

1 <= n <= 231 - 1

"""
from functools import lru_cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        self.res = n

        @lru_cache(None)
        def dfs(i):
            if i == 1: return 0
            if i & 1:
                return 1 + min(dfs(i + 1), dfs(i - 1))
            else:
                return 1 + dfs(i // 2)

        return dfs(n)
