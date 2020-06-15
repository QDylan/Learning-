# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/15 17:39
 @Author  : QDY
 @FileName: 32. 最长有效括号_动态规划_栈_hard.py

    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

    示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"

    示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"

"""


class Solution:
    def longestValidParentheses(self, s):
        # # 1.利用栈 判断到目前为止扫描的子字符串的有效性
        # stack,res = [-1],0  # 先将-1放入栈中
        # for i in range(len(s)):
        #     if s[i] == '(':  # 对于遇到的每个'(' ，我们将它的下标放入栈中
        #         stack.append(i)
        #     else:  # 遇到')'时，弹出栈顶元素
        #         stack.pop()
        #         if stack:  # 将当前元素与当前栈顶元素作差，得出当前有效括号字符串的长度
        #             res = max(res,i-stack[-1])
        #         else:
        #             stack.append(i)
        # return res

        # # 2.动态规划
        # # dp[i]=以s[i]结尾的子串的有效括号长度，'（'对应一定为0
        # # 只当s[i]==')'时更新
        # # 1.s[i-1]=='('时，形成()，dp[i] = dp[i-2]+2
        # # 2.s[i-1]=='）',形成...))
        # #   若s[i-dp[i-1]-1]='(',那么s[i-1]也是一个有效括号字符的结尾
        # #   dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        # n = len(s)
        # dp = [0]*n
        # res = 0
        # for i in range(1,n):
        #     if s[i]==')':
        #         if s[i-1]=='(': # 形成()
        #             dp[i] = dp[i-2]+2
        #         elif i>dp[i-1] and s[i-dp[i-1]-1]=='(':
        #             dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        #     res = max(res,dp[i])
        # return res

        # 3.从左往右，从右往左分别扫描一次,找出最长的有效字符串
        left, right = 0, 0  # 分别记录当前有效括号字符中出现了多少次左括号和右括号
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if right > left:  # 当前字符串加上s[i]是无效的
                    left, right = 0, 0  # 重新计数
                elif right == left:
                    res = max(res, left + right)

        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                if left > right:
                    left, right = 0, 0
                elif left == right:
                    res = max(res, left + right)
        return res
