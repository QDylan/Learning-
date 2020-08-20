# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/20 11:55
 @Author  : QDY
 @FileName: 316. 去除重复字母.py
 @Software: PyCharm
"""
"""
    给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
    需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
    示例 1:
    输入: "bcabc"
    输出: "abc"
    
    示例 2:
    输入: "cbacdcbc"
    输出: "acdb"

"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        len_s = len(s)
        res, used = [], set()
        for i in range(len_s):
            if s[i] not in used:  # 遇到一个新字符 如果比栈顶小 并且在新字符后面还有和栈顶一样的 就把栈顶的字符抛弃了
                while res and s[i] < res[-1] and counter[res[-1]] >= 1:  # counter[c]记录s[i:]还有多少个c字符
                    used.discard(res.pop())
                res.append(s[i])
                used.add(s[i])
            counter[s[i]] -= 1

        return ''.join(res)
