# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 13:46
 @Author  : QDY
 @FileName: 40. 组合总和 II_DFS.py

    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。

    说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。 

    示例 1:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

    示例 2:
    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
      [1,2,2],
      [5]
    ]

"""


class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates: return []
        res = []
        candidates.sort()
        while candidates and candidates[-1] > target:
            candidates.pop()
        # print(candidates)
        length = len(candidates)

        def dfs(start, nums, sum_):
            nonlocal res
            if sum_ == target:
                res.append(nums)
            elif sum_ > target or start == length:
                return
            else:
                for j in range(start, length):
                    if not (j > start and candidates[j] == candidates[j - 1]):  # 避免重复
                        dfs(j + 1, nums + [candidates[j]], sum_ + candidates[j])

        for i in range(length):
            if not (i > 0 and candidates[i] == candidates[i - 1]):  # 避免重复
                dfs(i + 1, [candidates[i]], candidates[i])
        return res
