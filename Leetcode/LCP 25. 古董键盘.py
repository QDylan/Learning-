# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-22 11:05
 @Author  : QDY
 @FileName: LCP 25. 古董键盘.py
 @Software: PyCharm
"""
"""
小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 a~z 可以按下，且每个字母最多仅能被按 k 次。
小扣随机按了 n 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。

示例 1：
输入：k = 1, n = 1
输出：26
解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z"

示例 2：
输入：k = 1, n = 2
输出：650
解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy"

提示：
1 <= k <= 5
1 <= n <= 26*k

"""
from math import factorial
from functools import lru_cache


class Solution:
    def keyboard(self, k: int, n: int) -> int:

        @lru_cache(None)
        def C(r, n):  # 求组合数
            if r > n // 2: return C(n - r, n)
            return factorial(n) // (factorial(n - r) * factorial(r))

        dp = [0] * (n + 1)  # 多重背包问题，26个物品，每个物品有k个，占用空间为1，背包空间为n
        dp[0] = 1
        for i in range(26):  # 考虑字母数量
            for j in range(n, 0, -1):  # 当前背包的容量为j
                for x in range(1, k + 1):  # 放入x个当前字母i
                    if x > j: break  # 背包容量不足，跳出
                    # 前i-1个字母用了j-x个空间有dp[j-x]种情况，剩余x个空间的位置从j个空间中选择
                    dp[j] += C(x, j) * dp[j - x]  #
                    dp[j] %= 1000000007
                if i == 25 and j == n: return dp[-1]  #
