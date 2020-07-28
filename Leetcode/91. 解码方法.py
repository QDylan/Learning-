# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/28 10:12
 @Author  : QDY
 @FileName: 91. 解码方法.py
 @Software: PyCharm
"""
"""
    一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。

    示例 1:
    输入: "12"
    输出: 2
    解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

    示例 2:
    输入: "226"
    输出: 3
    解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

"""


class Solution:
    def numDecodings(self, s):
        """
        当s[i-1]不是“1”或“2”的时候，证明s[i]不可以和s[i-1]联合解码
            当s[i]是 “0”的时候，s[i]无法解码，返回0
            当s[i]不是“0”的时候，s[i]位置独立解码，此时v[i]=v[i-1]
        当s[i-1]是“1”或“2”的时候，证明s[i]可以和s[i-1]联合解码
            当s[i]是 “0”的时候，s[i]一定要与s[i-1]一起解码，此时v[i]=v[i-2]
            当s[i]不是“0”的时候
                如果s[i-1]s[i]组成的数字小于等于26，则可以联合解码，v[i]=v[i-1]+v[i-2]
                否则，还是不可以联合解码，s[i]独立解码，v[i]=v[i-1]
        """
        length = len(s)
        if length == 0 or s[0] == '0':
            return 0
        else:
            dp0 = 1
        if length == 1: return 1
        if s[1] != '0' and (s[0] == '1' or (s[0] == '2' and s[1] <= '6')):
            dp1 = 2
        elif s[1] == '0' and s[0] > '2':
            dp1 = 0
        else:
            dp1 = 1

        for i in range(2, len(s)):
            if s[i] != '0' and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                # i-1与i可以联合
                dp2 = dp0 + dp1
            elif s[i - 1] != '1' and s[i - 1] != '2':
                if s[i] == '0':
                    return 0
                else:
                    dp2 = dp1
            else:
                if s[i] == '0':
                    dp2 = dp0
                else:
                    dp2 = dp1
            dp0, dp1 = dp1, dp2

        return dp1
