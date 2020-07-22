# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/22 18:09
 @Author  : QDY
 @FileName: 301. 删除无效的括号_BFS.py
 @Software: PyCharm
"""
"""
    删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
    说明: 输入可能包含了除 ( 和 ) 以外的字符。

    示例 1:
    输入: "()())()"
    输出: ["()()()", "(())()"]
    示例 2:
    输入: "(a)())()"
    输出: ["(a)()()", "(a())()"]

    示例 3:
    输入: ")("
    输出: [""]

"""


class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(strs):  # 判断一组括号是否合法
            cnt = 0
            for c in strs:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0: return False
            return cnt == 0

        # BFS
        level = {s}
        while True:
            valid_str = list(filter(is_valid, level))  # 筛选出level中所有合法的字符串

            if valid_str: return valid_str  # 如果当前valid_str是非空的，说明已经有合法的产生了,删除的数量最少

            next_level = set()  # 删除一个括号后的下一组字符串
            for item in level:
                for i in range(len(item)):
                    if item[i] in {'(', ')'}:  # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level
