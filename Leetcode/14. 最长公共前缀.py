# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/15 10:04
 @Author  : QDY
 @FileName: 14. 最长公共前缀.py

    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串""。

    示例1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        str1, str2 = max(strs), min(strs)
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                return str2[:i]
        return str2
