# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/12 23:31
 @Author  : QDY
 @FileName: 1478. 安排邮筒_动态规划_hard.py

    给你一个房屋数组houses和一个整数k，其中houses[i]是第 i栋房子在一条街上的位置，现需要在这条街上安排 k个邮筒。
    请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。
    答案保证在 32 位有符号整数范围以内。

    示例 1：
    输入：houses = [1,4,8,10,20], k = 3
    输出：5
    解释：将邮筒分别安放在位置 3， 9 和 20 处。
    每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。

    示例 2：
    输入：houses = [2,3,5,12,18], k = 2
    输出：9
    解释：将邮筒分别安放在位置 3 和 14 处。
    每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。

    示例 3：
    输入：houses = [7,4,6,1], k = 1
    输出：8

    示例 4：
    输入：houses = [3,6,14,10], k = 4
    输出：0

    提示：
    n == houses.length
    1 <= n<= 100
    1 <= houses[i] <= 10^4
    1 <= k <= n
    数组houses中的整数互不相同。

"""


class Solution:
    def minDistance(self, houses, k):
        n = len(houses)
        if n <= k: return 0
        houses.sort()
        one_box = [[0] * n for i in range(n)]
        for i in range(n):  # onebox[i][j]=第i+1个房屋到第j+1个房屋用一个信箱覆盖的距离和
            for j in range(i, n):
                mid = (i + j) // 2
                for _ in range(i, j + 1):  # 信箱必定在中间位置
                    one_box[i][j] += abs(houses[_] - houses[mid])
        # print(one_box)
        dp = [0] + one_box[0]  # 放1个箱子的情形
        for j in range(2, k + 1):  # dp[i] 记录前i个房子用j个信箱的最小距离和
            for i in range(n, j, -1):  # 前i个房屋，放j个信箱 (i>j)
                for x in range(j - 1, i):  # 枚举第j个信箱覆盖的房屋范围x，x从j-1到i-1
                    # 用j-1个信箱覆盖前x个房屋，第j个信箱覆盖第x+1到i个房屋
                    dp[i] = min(dp[x] + one_box[x][i - 1], dp[i])
            dp[j] = 0  # j个信箱可以完全覆盖前j个房屋，距离为0
        # print(dp)
        return dp[n]
