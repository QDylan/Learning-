# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 13:46
 @Author  : QDY
 @FileName: 40. 组合总和 II_DFS.py

    给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
    candidates中的每个数字在每个组合中只能使用一次。

    说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。

    示例1:
    输入: candidates =[10,1,2,7,6,1,5], target =8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

    示例2:
    输入: candidates =[2,5,2,1,2], target =5,
    所求解集为:
    [
     [1,2,2],
     [5]
    ]

"""


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        N = len(candidates)
        res = []

        def dfs(cur, cur_sum, index):
            if cur_sum == target:
                res.append(cur)
                return
            for i in range(index + 1, N):
                if i > index + 1 and candidates[i] == candidates[i - 1]: continue
                nxt_sum = cur_sum + candidates[i]
                if nxt_sum > target: break
                dfs(cur + [candidates[i]], nxt_sum, i)

        dfs([], 0, -1)
        return res
