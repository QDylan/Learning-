# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-12 15:43
 @Author  : QDY
 @FileName: ZJ_poj2411_状态压缩DP.py
 @Software: PyCharm
"""
"""
给定n*m的方格矩阵，用1*2的矩形去填充，求有多少种填充方案

例：
输入 n=2,m=3
输出 3

状态压缩
横着贴砖：(i,j)=(i,j+1)=1
竖着贴砖：(i,j)=0 (i+1,j)=1
最后一行都是1
dp[i][j] = 第i行，状态为j时，所能采取的方案数
"""


def init(s):
    while s:
        if s & 1:
            s >>= 1
            if s & 1:
                s >>= 1
            else:
                return False
        else:
            s >>= 1
    return True


def check(cur, prev, m):
    j = 0
    while j < m:
        if cur & 1:  # cur的第j位是1
            cur >>= 1
            if prev & 1:  # prev的第j位也是1，判断cur的第j位是不是横贴的右边一位
                prev >>= 1
                if j < m - 1 and cur & 1 and prev & 1:
                    j += 2
                    cur >>= 1
                    prev >>= 1
                else:
                    return False
            else:  # prev的第j位是0，表示竖贴
                prev >>= 1
                j += 1
        else:  # cur的第j位是0，则prev的第j位必须是1
            cur >>= 1
            if prev & 1:
                prev >>= 1
                j += 1
            else:
                return False
    return True


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n, m = 10, 10

    if n < m:
        n, m = m, n
    tot = 2 ** m
    if n * m % 2 != 0:
        print(0)
    elif m == 1:
        print(1)
    else:

        dp = [[0] * (2 ** m) for _ in range(n)]
        # dp[n - 1][tot - 1] = 1
        for s in range(tot):
            if init(s): dp[0][s] = 1  # 初始化第一层
        for i in range(1, n - 1):
            for j in range(tot):  # 第i行的状态
                for k in range(tot):  # 第i-1行的状态
                    if dp[i - 1][k] and check(j, k, m):
                        dp[i][j] += dp[i - 1][k]
        for k in range(tot):  # 最后一层必须全是1
            if dp[n - 2][k] and check(tot - 1, k, m):
                dp[n - 1][tot - 1] += dp[n - 2][k]
        # print(dp)
        print(dp[-1][-1])
