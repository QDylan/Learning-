# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/2 14:54
 @Author  : QDY
 @FileName: 5. 最长回文子串_中心扩散_动态规划_马拉车算法.py

    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设s 的最大长度为 1000。

    示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

    示例 2：
    输入: "cbbd"
    输出: "bb"

"""


class Solution:
    # # 中心扩散算法：expand around center
    # def EAC(self,s,left,right):
    #     while left>=0 and right<len(s) and s[left]==s[right]:
    #         left -= 1
    #         right += 1
    #     return right-left-1

    def longestPalindrome(self, s):
        len_s = len(s)
        if len_s <= 1: return s
        max_rad = 0
        res_center = s[0]
        # Manacher算法
        # 1.预处理字符串，插入#使都变成奇数个字符：accaba-> #a#c#c#a#b#a#
        new_s = '#'
        for i in s:  # 原数组id = (rad_id-1)//2
            new_s += i + '#'

        len_ns = len(new_s)  # 新的字符串长度
        rad = [0] * len_ns  # 数组rad 记录了新字符串中以每个字符为中心的回文子串的信息
        c = 1  # 记录回文的中心位置 center
        right = 1  # 记录回文的最右位置
        for i in range(1, len_ns - 1):  # 2.从左到右依次遍历,手动计算的方法仍是中心扩散
            # 2.1
            if right > i:  # 对于在右边界以内的点
                # 可以利用之前找到的 以c为中心，右边界为right的最长回文串，优化初始的搜索半径
                # 利用回文的对称性，i关于c的对称点为i_=2*c-i
                # 在回文串s_c = s[c-rad[c]:c+rad[c]+1]中，
                # 以中心c右边的某个点i为中心的回文子串半径>=i关于c对称的位置i_的最大回文半径
                # 还要有rad[i_mirror]<=right-i，因为在i在回文串s_c中最多只能扩展到右边界right
                rad[i] = min(right - i, rad[2 * c - i])
            else:  # i到达右边界right的情况
                rad[i] = 0
            # 2.2 已知new_s[i-rad[i]:i+rad[i]+1]为回文串，尝试中心扩散能否找到更大的回文半径
            while i + 1 + rad[i] < len_ns and i - 1 - rad[i] >= 0 and new_s[i + 1 + rad[i]] == new_s[i - 1 - rad[i]]:
                rad[i] += 1
            # 2.3
            if i + rad[i] > right:  # 若以new_s[i]为中心的最长回文右边界超过了right
                c = i  # 更新中心
                right = i + rad[i]  # 更新右边界
                if rad[i] > max_rad:
                    max_rad = rad[i]
                    res_center = i

        res = s[(res_center-max_rad-1)//2:(res_center+max_rad-1)//2+1]






        # # EAC
        # start, end = 0, 0
        # for i in range(len_s):
        #     length = max(self.EAC(s,i,i),self.EAC(s,i,i+1))
        #     if length>end-start:
        #         start = i - (length - 1) // 2
        #         end = i + length // 2
        # return s[start:end+1]

        # # 动态规划
        # len_s = len(s)
        # if len_s<=1:return s
        # dp = [[True]*len_s]
        # res = s[0]
        # dp.append([s[i]==s[i+1] for i in range(len_s-1)])
        # if True in dp[1]:
        #     start = dp[1].index(True)
        #     res = s[start:start+2]
        # if len_s <= 2:
        #     return res

        # for i in range(2, len_s): # 从3个字符开始
        #     cur_dp = []
        #     for j in range(len_s-i):
        #         cur_dp.append(dp[0][j+1] and s[j]==s[j+i])
        #     dp[0],dp[1] = dp[1], cur_dp
        #     if True in cur_dp:
        #         start = cur_dp.index(True)
        #         res = s[start:start+i+1]
        # return res
        return res
