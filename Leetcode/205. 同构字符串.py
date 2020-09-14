# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-14 10:07
 @Author  : QDY
 @FileName: 205. 同构字符串.py
 @Software: PyCharm
"""
"""
给定两个字符串s和t，判断它们是否是同构的。

如果s中的字符可以被替换得到t，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true
说明:
你可以假设s和 t 具有相同的长度。

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        hs = {}
        for i in range(n):
            if s[i] not in hs:
                hs[s[i]] = t[i]
            elif hs[s[i]] != t[i]:
                return False
        return len(set(hs.keys())) == len(set(hs.values()))
