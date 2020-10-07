# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-07 19:18
 @Author  : QDY
 @FileName: 编辑距离_不同权重.py
 @Software: PyCharm
"""
"""
给定两个字符串str1和str2，再给定三个整数ic，dc和rc，分别代表插入、删除和替换一个字符的代价，请输出将str1编辑成str2的最小代价。
"""

class Solution:
    def minEditCost(self, str1, str2, ic, dc, rc):
        # write code here
        len1, len2 = len(str1), len(str2)
        dp = [i * ic for i in range(len2 + 1)]
        for i in range(1, len1 + 1):
            prev, dp[0] = dp[0], i * dc
            for j in range(1, len2 + 1):
                tmp = dp[j]
                rrc = rc
                if str1[i - 1] == str2[j - 1]:
                    rrc = 0
                dp[j] = min(dp[j - 1] + ic, dp[j] + dc, prev + rrc)
                prev = tmp
        return dp[-1]
