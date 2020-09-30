# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-30 10:10
 @Author  : QDY
 @FileName: 520. 检测大写字母.py
 @Software: PyCharm
"""
"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:
输入: "USA"
输出: True

示例 2:
输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
        # if not word:return True
        # upper = True if word[0].isupper() else False
        # cnt, n = 0, len(word)
        # for c in word:
        #     if c.isupper():cnt += 1
        # return cnt==0 or cnt==n or (upper and cnt==1)
