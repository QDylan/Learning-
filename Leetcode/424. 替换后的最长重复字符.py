# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-15 10:20
 @Author  : QDY
 @FileName: 424. 替换后的最长重复字符.py
 @Software: PyCharm
"""
"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换k次。
在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过104。

示例 1:
输入:
s = "ABAB", k = 2
输出:
4
解释:
用两个'A'替换为两个'B',反之亦然。

示例 2:
输入:
s = "AABABBA", k = 1
输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N, cur_max, res = len(s), 0, 1
        if k >= N: return N
        cnt = defaultdict(int)  # 记录 滑动窗口中 每个字母的出现次数
        left, right = 0, 0  # 滑动窗口的左右边界
        while right < N:  # 不断扩大右边界
            cnt[s[right]] += 1
            cur_max = max(cur_max, cnt[s[right]])  # 获取窗口中最多的字母的数量
            while right - left + 1 > cur_max + k:  # 是否能k次替换把窗口中所有字母变成相同
                cnt[s[left]] -= 1  # 不能则缩短窗口的左边界
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
