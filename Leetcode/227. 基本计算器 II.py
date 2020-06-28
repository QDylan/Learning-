# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 18:19
 @Author  : QDY
 @FileName: 227. 基本计算器 II.py

    实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

    示例 1:
    输入: "3+2*2"
    输出: 7

    示例 2:
    输入: " 3/2 "
    输出: 1

    示例 3:
    输入: " 3+5 / 2 "
    输出: 5
    说明：

    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。

"""


class Solution:
    def calculate(self, s):
        res = []
        len_s = len(s)
        i = 0
        while i < len_s:
            if s[i].isdigit():
                j = i
                while i < len_s and s[i].isdigit():
                    i += 1
                num = int(s[j:i])
                if not res:
                    res.append(num)
                else:
                    sgn = res.pop()
                    if sgn == '+':
                        res.append(num)
                    elif sgn == '-':
                        res.append(-num)
                    elif sgn == '*':
                        res.append(res.pop() * num)
                    elif sgn == '/':
                        tmp = res.pop()
                        if tmp < 0:
                            res.append(-(-tmp // num))
                        else:
                            res.append(tmp // num)
            elif s[i] in {'+', '-', '*', '/'}:
                res.append(s[i])
                i += 1
            else:
                i += 1
        return sum(res)
