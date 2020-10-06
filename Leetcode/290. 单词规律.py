# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-06 11:21
 @Author  : QDY
 @FileName: 290. 单词规律.py
 @Software: PyCharm
"""
"""
给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。

这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设pattern只包含小写字母，str包含了由单个空格分隔的小写字母。

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split()
        # N = len(pattern)
        # if N != len(s):return False
        # p2s, s2p = {}, {}
        # for i in range(N):
        #     if pattern[i] not in p2s and s[i] not in s2p:
        #         p2s[pattern[i]] = s[i]
        #         s2p[s[i]] = pattern[i]
        #     elif pattern[i] in p2s and s[i] in s2p:
        #         if p2s[pattern[i]] != s[i] or s2p[s[i]] != pattern[i]:return False
        #     else:return False
        # return True

        def translate(lis):
            new = []
            dic = {}
            number = 1
            for i in lis:
                if i not in dic:
                    dic[i] = number
                    number += 1
                new.append(dic[i])
            return new

        pattern = list(pattern)
        s = s.split()
        return translate(pattern) == translate(s)
