# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/11 9:30
 @Author  : QDY
 @FileName: 1531. 压缩字符串 II.py
 @Software: PyCharm
"""
"""
    行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。
    例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。

    注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。
    给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。
    请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。

    示例 1：
    输入：s = "aaabcccd", k = 2
    输出：4
    解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。
    最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。

    示例 2：
    输入：s = "aabbaa", k = 2
    输出：2
    解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。

    示例 3：
    输入：s = "aaaaaaaaaaa", k = 0
    输出：3
    解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
     
    提示：
    1 <= s.length <= 100
    0 <= k <= s.length
    s 仅包含小写英文字母

"""


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int):
        len_s = len(s)
        if not s or k >= len(s): return 0

        def count(num):  # num个字母压缩后的数字的长度
            if num <= 1:
                return 0
            elif num > 1 and num < 10:
                return 1
            elif num >= 10 and num < 100:
                return 2
            else:
                return 3

        # 动态规划
        # dp[i][j] = s[:i]中最多选择删除j个字符后的 最短压缩字符长度
        # 若删除字符s[i-1] 则此时dp[i][j] = dp[i-1][j-1]
        # 若保留字符s[i-1] 则此后应尽量选择保留与s[i-1]相同的字符
        dp = [[float('inf')] * (k + 1) for i in range(len_s + 1)]
        dp[0][0] = 0  # base case
        for i in range(1, len_s + 1):
            for j in range(min(k, i) + 1):  # 删除的字符数不超过i
                if j < k:  # 若第j+1次删除字符s[i-1]，则压缩字符串长度为dp[i-1][j]
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j])
                same, delete = 0, 0
                for m in range(i, len_s + 1):
                    if s[m - 1] == s[i - 1]:
                        same += 1  # 相同的字符保留
                    else:  # 若与s[i-1]不相同，则删除该字符
                        delete += 1
                    if j + delete <= k:
                        dp[m][j + delete] = min(dp[m][j + delete], count(same) + 1 + dp[i - 1][j])
                    else:
                        break
        return dp[len_s][k]

        # size=len(s)
        # cnt,tmp = [0]*26, {0,1,9}
        # #dp[i][j][r]:选择了s中的i个字符(可以不连续但是按顺序) 最后一个字符是chr(j+97) 且最后一个字符在从后往前看 连续被选择了r次
        # #满足以上条件时压缩字符串的长度
        # dp=[[[float("inf") if i else 0]+[float("inf")]*(size-k) for _ in range(26)] for i in range(size-k+1)]
        # for i,j in enumerate(map(lambda x:ord(x)-97,s),1):
        #     cnt[j]+=1
        #     for r in range(min(i,size-k)-1,-1,-1): #从后往前 避免出现从前往后时 dp[r+1][...][...]的变化影响到dp[r+2][...][...]的情况
        #         for p in range(26):
        #             if cnt[p]: #剪枝 没有贡献
        #                 for q in range(min(r+1,cnt[p]+1)): #也是注意剪枝 否则就超时...
        #                     if j==p:
        #                         if q in tmp:
        #                             dp[r+1][j][q+1]=min(dp[r+1][j][q+1],dp[r][p][q]+1)
        #                         else:
        #                             dp[r+1][j][q+1]=min(dp[r+1][j][q+1],dp[r][p][q])
        #                     else:
        #                         dp[r+1][j][1]=min(dp[r+1][j][1],dp[r][p][q]+1)
        # return min(map(min,dp[-1]))
