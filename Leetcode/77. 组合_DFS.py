# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/24 22:25
 @Author  : QDY
 @FileName: 77. 组合_DFS.py

    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

    示例:
    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

"""
class Solution:
    def combine(self, n, k):
        res = []
        if not n or not k or n<k:return res

        def dfs(cur,nums):
            len_n = len(nums)
            if len_n==k:
                nonlocal res
                res.append(nums)
            else:
                for j in range(cur+1,n-k+len_n+2):  # 剪枝
                    dfs(j,nums+[j])

        for i in range(1,n-k+2):
            dfs(i,[i])

        return res