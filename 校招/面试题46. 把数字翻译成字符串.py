# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/9 8:54
 @Author  : QDY
 @FileName: 面试题46. 把数字翻译成字符串.py

    给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

    示例 1:
    输入: 12258
    输出: 5
    解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

"""


class Solution:
    def translateNum(self, num):
        # 动态规划
        # dp[i] = num[:i]有多少种翻译法
        # dp[0] = 1
        # if '0'<=num[i+1]<='2' and num[i+2] <='6':dp[i+2] = dp[i+1]+dp[i]
        # else: dp[i+2] = dp[i+1]
        num = str(num)
        n = len(num)
        if n <= 1: return n
        dp1 = 1
        if num[0] == '1' or (num[0] == '2' and num[1] < '6'):
            dp2 = 2
        else:
            dp2 = 1

        for i in range(2, n):
            if num[i - 1] == '1' or (num[i - 1] == '2' and num[i] < '6'):
                dp1, dp2 = dp2, dp1 + dp2
            else:
                dp1 = dp2
        return dp2
