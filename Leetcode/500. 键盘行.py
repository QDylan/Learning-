# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-06 11:09
 @Author  : QDY
 @FileName: 500. 键盘行.py
 @Software: PyCharm
"""
"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例：
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意：
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

"""


class Solution:
    def findWords(self, words):
        keys = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for w in words:
            res.append(w)
            for i in range(3):
                if w[0].lower() in keys[i]:
                    break
            for c in w:
                if c.lower() not in keys[i]:
                    res.pop()
                    break
        return resW
