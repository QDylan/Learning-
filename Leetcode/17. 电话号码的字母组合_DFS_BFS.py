# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/10 23:03
 @Author  : QDY
 @FileName: 17. 电话号码的字母组合_DFS_BFS.py

    给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    示例:

    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    说明:
    尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

"""


class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        # queue=['']
        # for i in digits:
        #     length = len(queue)
        #     for j in range(length):
        #         tmp = queue.pop(0)
        #         for k in d[i]:
        #             queue.append(tmp+k)
        # return queue

        length = len(digits)
        res = []

        def dfs(i, tmp_res):
            nonlocal res
            if i == length:
                res.append(tmp_res)
                return
            for j in d[digits[i]]:
                dfs(i + 1, tmp_res + j)

        dfs(0, '')
        return res
