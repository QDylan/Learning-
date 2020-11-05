# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-05 11:07
 @Author  : QDY
 @FileName: 526. 优美的排列.py
 @Software: PyCharm
"""
"""
假设有从 1 到 N 的N个整数，如果从这N个数字中成功构造出一个数组，
使得数组的第 i位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

第i位的数字能被i整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

示例1:
输入: 2
输出: 2
解释: 

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
  
说明:
N 是一个正整数，并且不会超过15。

"""
from functools import lru_cache


class Solution:
    def countArrangement(self, N: int) -> int:
        # self.res = 0
        # rest = {i for i in range(1,N+1)}
        # def dfs(i):
        #     if i==N+1:
        #         self.res += 1
        #         return
        #     for num in list(rest):
        #         if i%num==0 or num%i==0:
        #             rest.remove(num)
        #             dfs(i+1)
        #             rest.add(num)
        # dfs(1)
        # return self.res

        @lru_cache(None)
        def dfs(i, cur):  # 状态压缩 二进制数cur每一个位置n上表示n是否已被选用
            if i == N + 1: return 1
            res = 0
            for k in range(N):
                num = 1 << k
                if not num & cur and ((k + 1) % i == 0 or i % (k + 1) == 0):
                    res += dfs(i + 1, cur | num)
            return res

        return dfs(1, 0)