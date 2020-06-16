# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 20:38
 @Author  : QDY
 @FileName: 47. 全排列 II_DFS.py

    给定一个可包含重复数字的序列，返回所有不重复的全排列。

    示例:
    输入: [1,1,2]
    输出:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

"""


class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        visited = [False] * n

        def dfs(tmp_res=[]):
            nonlocal visited
            if len(tmp_res) == n:
                res.append(tmp_res)
            else:
                for i in range(n):
                    # 剪枝，避免重复，已经选过的不再选取；
                    # 若当前元素和前面一个元素相同，且前一个元素已经被选过，也不再选取
                    if not visited[i] and not (i > 0 and nums[i] == nums[i - 1] and visited[i - 1]):
                        visited[i] = True
                        dfs(tmp_res + [nums[i]])
                        visited[i] = False

        dfs()
        return res
