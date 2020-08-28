# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/28 16:32
 @Author  : QDY
 @FileName: 10.正则表达式匹配_动态规划_hard.py

    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

    示例 1:
    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。

    示例 2:
    输入:
    s = "aa"
    p = "a*"
    输出: true
    解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

    示例 3:
    输入:
    s = "ab"
    p = ".*"
    输出: true
    解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

    示例 4:
    输入:
    s = "aab"
    p = "c*a*b"
    输出: true
    解释:因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

    示例 5:
    输入:
    s = "mississippi"
    p = "mis*is*p*."
    输出: false
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
"""

class Solution:
    def isMatch(self,s,p):
        if not p:return not s
        len_s,len_p = len(s),len(p)
        # dp = [[False]*(len_p+1) for i in range(len_s+1)]  # dp[i][j] 表示 s 的前 i 个是否能被 p 的前 j 个匹配
        # dp[0][0] = True  # 表示空字符能匹配空字符
        # for j in range(1,len_p+1):  # 对于空字符串s[:0],只有x***能匹配,p[0]!='*'肯定不匹配
        #     dp[0][j] = j>1 and p[j-1]== '*' and dp[0][j-2]  # 初始化第一行
        # for i in range(1,len_s+1):
        #     for j in range(1,len_p+1):  # 对于s[:i]
        #         if p[j-1] != '*':  # p的当前字符不是*
        #             dp[i][j] = dp[i-1][j-1] and p[j-1] in {s[i-1], '.'}
        #         else:  # p[j-1]=='*'时
        #         # 1. 若p[:j-2]能匹配s[:i],则 p[j-2]p[j-1]可表示为空字符串, dp[i][j]=dp[i][j-2]
        #         # 2. 若p[:j]能匹配s[:i-1],那么加上一个s[i-1]是否还能匹配呢？
        #         #    若p[j-2]能与s[i-1]匹配，那么相当于在s[:i-1]结尾加上与结尾相同的字符
        #         #    p[j-2]p[j-1]==s[i-1]* 表示 多加上了一个s[i-1]，这种情况下也能成功匹配
        #             dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1],'.'})
        # # print(dp)
        # return dp[-1][-1]

        # dp1,dp2 = [True] ,[False]  # 节省空间
        # for j in range(1,len_p+1):
        #     dp1.append(j>1 and p[j-1]=='*' and dp1[j-2])
        # for i in range(1,len_s+1):
        #     for j in range(1,len_p+1):
        #         if p[j-1] != '*':
        #             dp2.append(dp1[j-1] and p[j-1] in {s[i-1], '.'})
        #         else:
        #             dp2.append(dp2[j-2] or (dp1[j] and p[j-2] in {s[i-1],'.'}))
        #     dp1,dp2 = dp2,[False]
        # return dp1[-1]

        # 逆向，dp[i][j]表示s[i:]能否被p[j:]匹配
        dp1,dp2 = [True] * (len_p+1), [False] * (len_p+1)
        for j in range(len_p-1,-1,-1):  # 初始话第一行，s=[]时
            dp1[j] = j<len_p-1 and p[j]!='*' and p[j+1]=='*' and dp1[j+2]
        for i in range(len_s-1,-1,-1):
            for j in range(len_p-1,-1,-1):
                if p[j] == '*':
                    dp2[j] = False
                else:
                    if j<len_p-1 and p[j+1]=='*':
                        dp2[j] = dp2[j+2] or (dp1[j] and p[j] in {s[i], '.'})
                    else:
                        dp2[j] = dp1[j+1] and p[j] in {s[i], '.'}
            dp1,dp2 = dp2,[False] * (len_p+1)
        return dp1[0]

    #     if not p:return not s
    #     len_s,len_p = len(s),len(p)
    #     if i is None and j is None:  # 从后往前匹配
    #         i,j = len_s-1,len_p-1
    #     # 终止条件
    #     if j==-1: return i == -1  # 当p匹配到头时，判断s是否也匹配到头
    #     if i==-1: # 若p没匹配到头，但s匹配到头了，可能是p的前两个字符是x*
    #     # 判断 是不是p的第二个字符为*
    #         return j>0 and p[j]=='*' and self.isMatch(s,p,i,j-2)

    #     if p[j] in {s[i], '.'}:
    #         return self.isMatch(s,p,i-1,j-1)
    #     elif p[j] == '*':  # *要和其前一个字符x一起匹配
    #     # 1.x*表示空字符串，将j往前移两位；2.s[i]与*号前的字符相匹配,x*可以表示s[i],令i往前移一位
    #         return self.isMatch(s,p,i,j-2) or (self.isMatch(s,p,i-1,j) and p[j-1] in {s[i], '.'})
    #     else:
    #         return False

    # def isMatch(self, s, p):
    #     if not p: # 若p空，则返回s是否为空
    #         return not s
    #     # 首个字符匹配，判断p[0]是否等于s[0]或为'.''
    #     first_match = bool(s) and p[0] in {s[0],'.'}
    #     if len(p) >= 2 and p[1]=='*':
    #         # 若p下一个字符是'*'且p中多于3个字符时
    #         #
    #         # 1. p[2:]与s匹配成功: p='a*xxx' or '.*xxx'
    #         # 2. 且s[1:]与p匹配成功
    #         if first_match: # 首个字符匹配成功 s='axxx' or 'bxxx'
    #             return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
    #         else:
    #             return self.isMatch(s, p[2:])
    #     else:
    #         if first_match:  # 若第一段字符匹配成功,递归地将剩下的匹配
    #             return self.isMatch(s[1:], p[1:])
    #         else:
    #             return False