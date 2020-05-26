# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/26 21:46
 @Author  : QDY
 @FileName: 1456. 定长子串中元音的最大数目_滑动窗口_前缀和.py

    给你字符串 s 和整数 k 。
    请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
    英文中的 元音字母 为（a, e, i, o, u）。

    示例 1：
    输入：s = "abciiidef", k = 3
    输出：3
    解释：子字符串 "iii" 包含 3 个元音字母。

    示例 2：
    输入：s = "aeiou", k = 2
    输出：2
    解释：任意长度为 2 的子字符串都包含 2 个元音字母。

    示例 3：
    输入：s = "leetcode", k = 3
    输出：2
    解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

    示例 4：
    输入：s = "rhythms", k = 4
    输出：0
    解释：字符串 s 中不含任何元音字母。

    示例 5：
    输入：s = "tryhard", k = 4
    输出：1

"""


class Solution:
    def maxVowels(self, s, k):
        res = 0
        tmp = {'a', 'e', 'i', 'o', 'u'}
        if len(s) <= k:  # 字符串长度小于k的情形，直接计算s中有多少个元音
            for i in range(len(s)):
                if s[i] in tmp:
                    res += 1
            return res
        for i in range(k):  # 滑动窗口，初始化一个长度为k的窗口，记录其元音数量
            if s[i] in tmp:
                res += 1
        if res == k:
            return res
        tmp_res = res  # 记录当前窗口中的元音数量
        for i in range(k, len(s)):  # 窗口向右移动，每次删除最左一个元素，添加右边一个元素
            if s[i - k] in tmp:  # 若删除元素是元音，则tmp_res-1
                tmp_res -= 1
            if s[i] in tmp:  # 若添加元素是元音，则tmp_res+1
                tmp_res += 1
            res = max(res, tmp_res)
            if res == k: return res  # res不可能超过k
        return res

        # prefix_sum = [0]*(len(s)+1)  # 前缀和,prefix_sum[i]=s[:i]中的元音数量
        # for i in range(1,len(s)+1):
        #     prefix_sum[i] = prefix_sum[i-1] + (1 if s[i-1] in tmp else 0)
        # res = 0
        # for i in range(len(s)-k+1):  # prefix_sum[i+k]-prefix_sum[i]=s[i:i+k]中的元音数量
        #     res = max(res,prefix_sum[i+k]-prefix_sum[i])
        #     if res == k:return k
        # return res
