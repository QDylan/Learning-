# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/14 12:17
 @Author  : QDY
 @FileName: 87. 扰乱字符串.py
 @Software: PyCharm
"""
"""
    给定一个字符串s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
    下图是字符串s1="great"的一种可能的表示形式。
    
        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t
    在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
    例如，如果我们挑选非叶节点"gr"，交换它的两个子节点，将会产生扰乱字符串"rgeat"。
    
        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t
    我们将"rgeat”称作"great"的一个扰乱字符串。
    同样地，如果我们继续交换节点"eat"和"at"的子节点，将会产生另一个新的扰乱字符串"rgtae"。
    
        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a
    我们将"rgtae”称作"great"的一个扰乱字符串。
    给出两个长度相等的字符串 s1 和s2，判断s2是否是s1的扰乱字符串。
    
    示例1:
    输入: s1 = "great", s2 = "rgeat"
    输出: true
    
    示例2:
    输入: s1 = "abcde", s2 = "caebd"
    输出: false

"""
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 != len2: return False
        # # 动态规划
        # # dp[i][j][l] = s1[i:i+l+1]与s2[j:j+l+1]是否可转换
        # dp = [[[False]*len1 for j in range(len1)] for i in range(len1)]
        # for i in range(len1):
        #     for j in range(len2):
        #         if s1[i] == s2[j]:
        #             dp[i][j][0] = True
        # for l in range(1,len1):
        #     for i in range(len1-l):
        #         for j in range(len2-l):
        #             for k in range(l):  # 遍历每个切分点
        #                 dp[i][j][l] = dp[i][j][k] and dp[i+k+1][j+k+1][l-1-k]
        #                 if dp[i][j][l]:break
        #                 dp[i][j][l] = dp[i][j+(l-k)][k] and dp[i+k+1][j][l-1-k]
        #                 if dp[i][j][l]:break
        # return dp[0][0][len1-1]

        # 递归
        if s1 == s2: return True
        c1, c2 = Counter(s1), Counter(s2)
        if c1 != c2: return False
        if len1 <= 2: return True
        for i in range(1, len1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False
