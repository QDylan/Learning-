# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/15 9:21
 @Author  : QDY
 @FileName: 96. 不同的二叉搜索树.py

    给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

    示例:

    输入: 3
    输出: 5
    解释:
    给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)  # 动态规划
        dp[0] = 1  # dp[i]= n个节点组成的二叉搜索树有多少种
        for i in range(1, n + 1):
            for j in range(i):  # 对于有i个节点的二叉搜索树
                # 以j+1为根节点时，左子树有j个节点，右子树有i-1-j个节点
                dp[i] += dp[j] * dp[i - 1 - j]  # 则以j+1为根节点的二叉搜索树有dp[j]*dp[i-1-j]种
        # print(dp)
        return dp[n]
