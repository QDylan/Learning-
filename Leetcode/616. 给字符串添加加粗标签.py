# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/25 20:52
 @Author  : QDY
 @FileName: 616. 给字符串添加加粗标签.py
 @Software: PyCharm
"""
"""
    给一个字符串 s 和一个字符串列表 dict ，你需要将在字符串列表中出现过的 s 的子串添加加粗闭合标签 <b> 和 </b> 。
    如果两个子串有重叠部分，你需要把它们一起用一个闭合标签包围起来。
    同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。

    样例 1：
    输入：
    s = "abcxyz123"
    dict = ["abc","123"]
    输出：
    "<b>abc</b>xyz<b>123</b>"

    样例 2：
    输入：
    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    输出：
    "<b>aaabbc</b>c"
     
    注意：
    给定的 dict 中不会有重复的字符串，且字符串数目不会超过 100 。
    输入中的所有字符串长度都在范围 [1, 1000] 内。

"""


class Solution:
    def addBoldTag(self, s: str, words):
        len_s, mask = len(s), [False] * len(s)
        for i in range(len_s):
            prefix = s[i:]
            for w in words:
                if prefix.startswith(w):  # s[i:]以某个单词开头
                    for j in range(i, min(i + len(w), len_s)):
                        mask[j] = True  # 将s[i:]中这个单词的部分标记为True
        # print(mask)
        res, i = '', 0
        while i < len_s:
            if mask[i]:
                res += '<b>'
                while i < len_s and mask[i]:
                    res += s[i]
                    i += 1
                res += '</b>'
            else:
                res += s[i]
                i += 1
        return res
