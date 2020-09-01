# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 10:10
 @Author  : QDY
 @FileName: 486. 预测赢家.py
 @Software: PyCharm
"""
"""
    给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，
    随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
    每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。
    直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
    
    给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
    
    示例 1：
    输入：[1, 5, 2]
    输出：False
    解释：一开始，玩家1可以从1和2中进行选择。
    如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
    所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
    因此，玩家 1 永远不会成为赢家，返回 False 。
    
    示例 2：
    输入：[1, 5, 233, 7]
    输出：True
    解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
         最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
    
    提示：
    1 <= 给定的数组长度<= 20.
    数组里所有分数都为非负数且不会大于 10000000 。
    如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。

"""
from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums) -> bool:
        n = len(nums)
        if n & 1 == 0: return True
        # prefix = [0]
        # for num in nums:
        #     prefix.append(num+prefix[-1])

        # @ lru_cache(None)
        # def dp(left,right,role):
        #     if left==right:
        #         return nums[left] if role==0 else 0
        #     if role == 0:
        #         return max(nums[left]+dp(left+1,right,1),nums[right]+dp(left,right-1,1))
        #     else:
        #         return prefix[right+1]-prefix[left]-dp(left,right,0)
        # role0 = dp(0,n-1,0)
        # role1 = prefix[n]-role0
        # return role0>=role1

        dp0 = [[0] * n for i in range(n)]
        dp1 = [[0] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            dp0[i][i] = nums[i]
            for j in range(i + 1, n):
                left = dp1[i + 1][j] + nums[i]
                right = dp1[i][j - 1] + nums[j]
                if left > right:
                    dp0[i][j], dp1[i][j] = left, dp0[i + 1][j]
                else:
                    dp0[i][j], dp1[i][j] = right, dp0[i][j - 1]
        return dp0[0][n - 1] >= dp1[0][n - 1]
