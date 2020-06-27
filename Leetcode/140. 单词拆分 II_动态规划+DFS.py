# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/27 16:51
 @Author  : QDY
 @FileName: 140. 单词拆分 II_动态规划+DFS.py

    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
    在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

    说明：
    分隔时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

    示例 1：
    输入:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    [
      "cats and dog",
      "cat sand dog"
    ]

    示例 2：
    输入:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    输出:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    解释: 注意你可以重复使用字典中的单词。

    示例 3：
    输入:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出:
    []

"""


class Solution:
    def wordBreak(self, s: str, wordDict):
        if not s: return []
        wordDict = set(wordDict)
        # dp[i][j] = s[i:j+1] is a word
        len_s = len(s)
        dp_check = [False] * len(s)  # 判断该字符串是否可以有效拆分
        dp = [[False] * len_s for i in range(len_s)]  #
        for j in range(len_s):
            if wordDict.__contains__(s[:j + 1]):
                dp_check[j] = True
                dp[0][j] = True
        for i in range(len_s):
            if dp_check[i]:
                for j in range(i, len_s):
                    if wordDict.__contains__(s[i + 1:j + 1]):
                        dp_check[j] = True
                        dp[i + 1][j] = True  # 找到每个单词的位置
        if not dp_check[-1]: return []

        res = []

        def dfs(i, tmp):
            nonlocal res
            if i == len_s:
                res.append(' '.join(tmp))
                return
            for j in range(i, len_s):
                if dp[i][j]:
                    dfs(j + 1, tmp + [s[i:j + 1]])

        for j in range(len_s):
            if dp[0][j]:
                dfs(j + 1, [s[:j + 1]])

        return res
