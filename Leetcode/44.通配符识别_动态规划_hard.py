# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/28 20:50
 @Author  : QDY
 @FileName: 44.通配符识别_动态规划_hard.py

    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。

    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

    示例 1:
    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。

    示例 2:
    输入:
    s = "aa"
    p = "*"
    输出: true
    解释: '*' 可以匹配任意字符串。

    示例 3:
    输入:
    s = "cb"
    p = "?a"
    输出: false
    解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

    示例 4:
    输入:
    s = "adceb"
    p = "*a*b"
    输出: true
    解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

    示例 5:
    输入:
    s = "acdcb"
    p = "a*c?b"
    输入: false
"""


class Solution:
    def isMatch(self, s, p):
        if not p: return not s
        len_s, len_p = len(s), len(p)

        # 回溯
        i = j = 0
        star_idx = s_tmp_idx = -1
        while i < len_s:
            if j < len_p and p[j] in {'?', s[i]}:
                i += 1
                j += 1
            elif j < len_p and p[j] == '*':
                star_idx = j  # 记录最后一个*出现的位置·
                s_tmp_idx = i  # 同时记录与这个*要匹配的字符在s中的位置
                j += 1  # i不增加，表示*表示空字符
            elif star_idx == -1:  # 若尚未记录*号，且字符不匹配，则返回False
                return False
            else:  # p[j]与s[i]不匹配，需要使用*号，回溯到最后一个*
                j = star_idx + 1  # j回溯到*号后一个位置
                i = s_tmp_idx + 1  # i回溯到后一个位置，表示*号要多表示一个字符串
                s_tmp_idx = i

        # 若s被匹配完后，p中字符还没用完，则应剩下的全都是*才能成功匹配
        return all(x == '*' for x in p[j:])

        # # 动态规划
        # dp1, dp2 = [True], [False]
        # for j in range(1,len_p+1):
        #     dp1.append(p[j-1]=='*' and (j==1 or (j>1 and dp1[j-1])))
        # print(dp1)
        # for i in range(1,len_s+1):
        #     for j in range(1,len_p+1):
        #         if p[j-1]=='*':
        #             if j==1:
        #                 dp2.append(True)
        #             else:
        #                 dp2.append(dp2[j-1] or dp1[j])
        #         else:
        #             dp2.append(dp1[j-1] and p[j-1] in {s[i-1],'?'})
        #     dp1,dp2 = dp2, [False]
        # return dp1[-1]

        # # 逆向，dp[i][j]表示s[i:]能否被p[j:]匹配
        # # dp[0][0] = True 表示空字符可以匹配空字符
        # dp1, dp2 = [True] * (len_p + 1), [False] * (len_p + 1)
        # for j in range(len_p - 1, -1, -1):  # 初始化第一行：p[j:]匹配空字符
        #     dp1[j] = p[j] == '*' and dp1[j + 1]  # 只有在前面匹配成功且当前p[j]=*的情况下才能匹配
        # for i in range(len_s - 1, -1, -1):  #
        #     for j in range(len_p - 1, -1, -1):
        #         if p[j] == '*':  # 当遇到*时
        #             if j == len_p - 1:  # 若是最后一个字符串，则一定能匹配
        #                 dp2[j] = True
        #             else:  # 若不是最后，则有两种情况能匹配成功
        #                 # 1. p[j+1:]能匹配s[i:]
        #                 # 2. p[j] 能匹配 s[i+1],令*号多匹配一个字符串s[i]即能成功匹配
        #                 dp2[j] = dp2[j + 1] or dp1[j]
        #         else:  # 若不是*，则p[j+1:]必须匹配s[i+1:]且p[j]=='?'or s[i]
        #             dp2[j] = dp1[j + 1] and p[j] in {'?', s[i]}
        #     dp1, dp2 = dp2, [False] * (len_p + 1)
        # return dp1[0]
