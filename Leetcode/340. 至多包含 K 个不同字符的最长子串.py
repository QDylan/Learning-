# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/25 16:01
 @Author  : QDY
 @FileName: 340. 至多包含 K 个不同字符的最长子串.py
 @Software: PyCharm
"""
"""
    给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

    示例 1:
    输入: s = "eceba", k = 2
    输出: 3
    解释: 则 T 为 "ece"，所以长度为 3。

    示例 2:
    输入: s = "aa", k = 1
    输出: 2
    解释: 则 T 为 "aa"，所以长度为 2。

"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        res, count = 1, defaultdict(int)
        left = 0  # 滑动窗口
        count[s[0]] = 1
        for right in range(1, len(s)):
            count[s[right]] += 1
            if len(count) <= k:
                res = max(res, right - left + 1)
            else:
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        count.pop(s[left])
                    left += 1
        return res
