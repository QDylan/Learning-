# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/25 8:49
 @Author  : QDY
 @FileName: 139. 单词拆分_动态规划.py

    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

    说明：
    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

    示例 1：
    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

    示例 2：
    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。

    示例 3：
    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        len_s = len(s)
        # 动态规划
        dp = [False]*len_s  # dp[i]=s[:i+1]是否能拆分出wordDict中的词
        for i in range(len_s):  # base case: dp[i]=s[:i+1]是否是wordDict中的词
            if wordDict.__contains__(s[:i+1]):
                dp[i] = True
        if dp[-1]:
            return True
        for i in range(len_s):
            if dp[i]:  # dp[j] = dp[i] and s[i+1:j+1] in wordDict
                for j in range(i+1,len_s):
                    if wordDict.__contains__(s[i+1:j+1]):
                        dp[j] = True
                if dp[-1]:
                    return True

        return False