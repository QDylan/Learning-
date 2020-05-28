# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/19 16:02
 @Author  : QDY
 @FileName: 72. 编辑距离_动态规划_hard.py

    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
 
    示例 1：
    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')

    示例 2：
    输入：word1 = "intention", word2 = "execution"
    输出：5
    解释：
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')
"""


class Solution:
    def minDistance(self, word1, word2) -> int:
        len1, len2 = len(word1), len(word2)
        # 动态规划
        # dp[i][j] 表示w1[:i]转换成w2[:j]需要的最小操作数
        # 压缩到两个一维
        dp1 = [j for j in range(len2 + 1)]  # dp[0][j] = j
        dp2 = [1]
        for i in range(1, len1 + 1):  # 计算w1[:i]转换到w2[:0],w2[:1]...,w2需要的最小操作数
            for j in range(1, len2 + 1):  # 计算dp[i][j]
                if word1[i - 1] == word2[j - 1]:  # 1.若w1[i-1]==w2[j-1]
                    dp2.append(dp1[j - 1])  # 则w1[:i]转换到w2[:j]在w1[:i-1]转换到w2[:j-1]的基础上不用做任何操作
                    # dp[i][j] = dp[i-1][j-1]
                else:
                    # 2. 若w1[i-1]!=w2[j-1]则需要执行 删除、替换、插入 其中一种操作
                    # 2.1 在w1[:i-1]转换到w2[:j]的基础上,
                    #   w2[:j]+w1[i-1] 删除结尾元素，dp[i][j] = dp[i-1][j] + 1
                    # 2.2 在w1[:i-1]转换到w2[:j-1]的基础上, 而新的结尾元素w1[i-1]!=w2[j-1]
                    #   将w1[i-1] 替换 为w2[j-1]：dp[i][j] = dp[i-1][j-1] + 1
                    # 2.3 在w1[:i]转换到w2[:j-1]的基础上,
                    #   将w2[:j-1]后面 插入 w2[j-1]：dp[i][j] = dp[i][j-1] + 1

                    # 取这三种情况的最小值，更新为w1[:i]转换到w2[:0]的最小操作数
                    dp2.append(min(dp1[j], dp1[j - 1], dp2[j - 1]) + 1)
            dp1, dp2 = dp2, [i + 1]

        return dp1[-1]

        # dp = [j for j in range(len2+1)]  # 进一步压缩，只是用一个一维数组
        # for i in range(1, len1 + 1):
        #     prev = dp[0]
        #     dp[0] = i
        #     for j in range(1, len2 + 1):  # w2[:j]
        #         tmp, prev = prev, dp[j]
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[j] = tmp
        #         else:
        #             dp[j] = min(dp[j], dp[j - 1], tmp) + 1
        # return dp[len2]
