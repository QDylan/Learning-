# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-11 10:01
 @Author  : QDY
 @FileName: 216. 组合总和 III.py
 @Software: PyCharm
"""

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []

        def dfs(cur, cur_sum, last_num):
            if len(cur) == k and cur_sum == n:
                res.append(cur)
                return
            elif cur_sum >= n or len(cur) > k:
                return

            for i in range(last_num + 1, 10):
                nxt_sum = cur_sum + i
                if nxt_sum > n: break
                dfs(cur + [i], nxt_sum, i)

        dfs([], 0, 0)
        return res
