# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-10 14:14
 @Author  : QDY
 @FileName: 678. 有效的括号字符串.py
 @Software: PyCharm
"""
"""
给定一个只包含三种字符的字符串：（，）和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 (必须有相应的右括号 )。
任何右括号 )必须有相应的左括号 (。
左括号 ( 必须在对应的右括号之前 )。
*可以被视为单个右括号 ) ，或单个左括号 (，或一个空字符串。
一个空字符串也被视为有效字符串。

示例 1:
输入: "()"
输出: True

示例 2:
输入: "(*)"
输出: True

示例 3:
输入: "(*))"
输出: True

注意:
字符串大小将在 [1，100] 范围内。

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        # 贪心
        lo, hi = 0, 0  # lo、hi表示「可能多余的左括号」，一个下界，一个上界
        for i in s:
            if i == '(':
                lo += 1
                hi += 1
            elif i == '*':
                if lo > 0: lo -= 1  # * 当做右括号，消耗掉左括号
                hi += 1  # * 当做左括号
            else:  # 遇到) 一定要消耗掉左括号
                if lo > 0: lo -= 1
                hi -= 1
            if hi < 0: return False  # 上界<0，说明右括号太多
        return lo == 0  # 下界>0,说明左括号太少

        # left, star = [], []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         left.append(i)
        #     elif s[i] == '*':
        #         star.append(i)
        #     else:
        #         if not left and not star:return False
        #         if left:
        #             left.pop()
        #         else:
        #             star.pop()
        # while left and star:
        #     if left[-1] > star[-1]:return False
        #     left.pop()
        #     star.pop()
        # return left==[]  # 多余的*可表示空字符
