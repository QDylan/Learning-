# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/10 10:43
 @Author  : QDY
 @FileName: 696. 计数二进制子串.py
 @Software: PyCharm
"""
"""
    给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
    重复出现的子串要计算它们出现的次数。

    示例 1 :
    输入: "00110011"
    输出: 6
    解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

    请注意，一些重复出现的子串要计算它们出现的次数。
    另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

    示例 2 :
    输入: "10101"
    输出: 4
    解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

    注意：
    s.length 在1到50,000之间。
    s 只包含“0”或“1”字符。

"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        if length <= 1: return 0
        prev, cur, res = 0, 1, 0  # prev记录前一种字符连续出现的次数
        for i in range(1, length):
            if s[i] == s[i - 1]:  # 当前字符与上一个字符相同
                cur += 1  # cur记录当前字符连续出现的次数
            else:  # 连续中断，将当前字符连续出现的次数cur赋给prev
                prev = cur
                cur = 1  # cur重置为1
            if prev >= cur:  # 当前一种字符的连续出现次数prev>=cur时
                res += 1  # 可以找到一组子串，每种字符连续的长度为cur
        return res
