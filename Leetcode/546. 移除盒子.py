# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/15 10:06
 @Author  : QDY
 @FileName: 546. 移除盒子.py
 @Software: PyCharm
"""
"""
    给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
    你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。
    每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
    当你将所有盒子都去掉之后，求你能获得的最大积分和。

    示例：
    输入：boxes = [1,3,2,2,2,3,4,3,1]
    输出：23
    解释：
    [1, 3, 2, 2, 2, 3, 4, 3, 1] 
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
    ----> [1, 3, 3, 3, 1] (1*1=1 分) 
    ----> [1, 1] (3*3=9 分) 
    ----> [] (2*2=4 分)
     
    提示：
    1 <= boxes.length <= 100
    1 <= boxes[i] <= 100

"""
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes) -> int:

        # # dp[l][r][k] = boxes[l:r+1]右边加上k个boxes[r]的最大积分
        # N = len(boxes)
        # dp = [[[0]*N for i in range(N)] for j in range(N)]
        # def helper(l,r,k):
        #     nonlocal dp
        #     if l>r:return 0
        #     if dp[l][r][k] != 0: return dp[l][r][k]
        #     while r > 1 and boxes[r] == boxes[r-1]:  # 若boxes[l:r+1]右边有连续的boxes[r]元素
        #         r -= 1  # 将r减小，将k增大，使得boxes[r]!=boxes[r-1]
        #         k += 1
        #     dp[l][r][k] = helper(l, r-1, 0) + (k+1)**2  # dp[l][r-1][0]+(k+1)*(k+1)
        #     for i in range(l,r):  # 在l~r中找到与boxes[r]相同的元素boxes[i] 作为分割点
        #         if boxes[i] == boxes[r]:
        #             # dp[l][i][k+1]: boxes[l:i+1]右边再接k+1个boxes[i] 的最大得分
        #             # 这k+1个boxes[i] 为 boxes[l:r+1]后接的k个 加上 boxes[r]
        #             # dp[i+1][r-1]: boxes[i+1:r] 的最大得分
        #             dp[l][r][k] = max(dp[l][r][k],helper(l,i,k+1)+helper(i+1,r-1,0))
        #     return dp[l][r][k]
        # return helper(0,N-1,0)

        @lru_cache(None)
        def helper(l, r, k):
            if l > r: return 0
            while r > 1 and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            res = helper(l, r - 1, 0) + (k + 1) ** 2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, helper(l, i, k + 1) + helper(i + 1, r - 1, 0))
            return res

        return helper(0, len(boxes) - 1, 0)
