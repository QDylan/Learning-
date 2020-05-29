# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/29 9:05
 @Author  : QDY
 @FileName: 28. 实现 strStr()_KMP算法.py

    实现 strStr() 函数。
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
    如果不存在，则返回  -1。

    示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2

    示例 2:
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    说明:

    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        # 暴力
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i]==needle[0] and haystack[i:i+len(needle)]==needle:
        #         return i
        # return -1

        len_h, len_n = len(haystack), len(needle)
        # KMP算法
        # lps Longest Prefix and Suffix最长公共前缀和后缀（前缀和后缀不能为同一字符串）
        lps = [0] * len_n  # Longest Prefix and Suffix,单个字符时为0
        # LPS[i] 记录needle[:i+1]的lps的长度
        i, length = 1, 0  # length 记录needle[:i]的lps中的长度
        while i < len_n:  # needle[length]就是前缀的后一个字符
            if needle[i] == needle[length]:  # 最后一个字符与lps后一个字符相等
                length += 1  # 则可以增加最长公共前缀后缀的长度
                lps[i] = length  # 记录该长度进lps
                i += 1
            elif length > 0:  # 若不相等，则length=needle[:length]的lps长度
                # 原理：找到之前的最长前缀needle[:length]的lps是什么
                # 该lps实际上是第二长（次级）的lps  ----- 关键
                # 若lps后一个字符与needle[i]还不相等，则继续取该lps的lps
                # 直到length==0为止，表示要将needle[i]与首字符匹配
                length = lps[length - 1]
                # 例如'aabaaa'最后一项之前，lps=[0,1,0,1,2],length=2
                # needle[2]=b!=needle[i]=a
                # 找到'aa' 的lps为a,长度为1，而needle[1]=neddle[i]=a
                # 所以length = 2
            else:
                i += 1

        i, j = 0, 0
        while i < len_h:
            if haystack[i] == needle[j]:  # 成功匹配
                i += 1
                j += 1
                if j == len_n:
                    return i - len_n
            elif j > 0:  # 当不匹配且j>0时，尝试跳跃
                j = lps[j - 1]  # 将j跳跃到needle[:j]的lps的后一个位置
                # 因为若匹配到j才失败,且needle[:j]有lps
                # 则说明haystack[i-len(lps):i]==lps,可以不用重复匹配
            else:  # 第一个就不匹配，不用跳跃
                i += 1

        return -1
