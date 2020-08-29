# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-29 18:11
 @Author  : QDY
 @FileName: 438. 找到字符串中所有字母异位词.py
 @Software: PyCharm
"""
"""
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

    说明：
    字母异位词指字母相同，但排列不同的字符串。
    不考虑答案输出的顺序。

    示例 1:
    输入:
    s: "cbaebabacd" p: "abc"
    输出:
    [0, 6]

    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

     示例 2:
    输入:
    s: "abab" p: "ab"
    输出:
    [0, 1, 2]

    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

"""
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):  # 滑动窗口
        len_p, len_s = len(p), len(s)
        if len_p > len_s: return []
        # cnt_p = Counter(p)
        # cnt = Counter(s[:len_p])
        # res = []
        # if cnt == cnt_p:res.append(0)
        # for i in range(len_p,len_s):
        #     cnt[s[i]] += 1
        #     cnt[s[i-len_p]] -= 1
        #     if cnt[s[i-len_p]]==0:cnt.pop(s[i-len_p])
        #     if cnt==cnt_p:res.append(i-len_p+1)
        # return res
        cnt, cnt_p = [0] * 26, [0] * 26
        for c in p:
            cnt_p[ord(c) - 97] += 1
        for i in range(len_p):
            cnt[ord(s[i]) - 97] += 1
        res = []
        if cnt == cnt_p: res.append(0)
        for i in range(1, len_s - len_p + 1):
            cnt[ord(s[i - 1]) - 97] -= 1
            cnt[ord(s[i + len_p - 1]) - 97] += 1
            if cnt == cnt_p: res.append(i)
        return res
