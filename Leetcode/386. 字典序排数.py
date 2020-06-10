# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/10 9:50
 @Author  : QDY
 @FileName: 386. 字典序排数.py

    给定一个整数 n, 返回从 1 到 n 的字典顺序。

    例如，

    给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9]
"""


class Solution:
    def lexicalOrder(self, n):

        res = []

        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            for j in range(10):  # 遍历0 ~ 9
                dfs(cur * 10 + j)

        for i in range(1, 10):  # 遍历1 ~ 9
            dfs(i)
        return res


