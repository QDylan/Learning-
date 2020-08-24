# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/24 9:04
 @Author  : QDY
 @FileName: 459. 重复的子字符串.py
 @Software: PyCharm
"""
"""
    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

    示例 1:
    输入: "abab"
    输出: True
    解释: 可由子字符串 "ab" 重复两次构成。

    示例 2:
    输入: "aba"
    输出: False

    示例 3:
    输入: "abcabcabcabc"
    输出: True
    解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 假设s中存在s_重复出现n次，则s=n*s_,2s=2n*s_, s必定在2s[1:-1]中出现
        return s in (s + s)[1:-1]
        # length = len(s)
        # for i in range(1,length//2+1):
        #     if length % i == 0:
        #         valid = True
        #         for j in range(i,length-i+1,i):
        #             # print(s[:i],s[j:j+i])
        #             if s[j:j+i] != s[:i]:
        #                 valid = False
        #                 break
        #         if valid:return True
        # return False
