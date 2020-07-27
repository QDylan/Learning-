# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/27 11:41
 @Author  : QDY
 @FileName: 161. 相隔为 1 的编辑距离.py
 @Software: PyCharm
"""
"""
    给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

    注意：
    满足编辑距离等于 1 有三种可能的情形：
    往 s 中插入一个字符得到 t
    从 s 中删除一个字符得到 t
    在 s 中替换一个字符得到 t

    示例 1：
    输入: s = "ab", t = "acb"
    输出: true
    解释: 可以将 'c' 插入字符串 s 来得到 t。

    示例 2:
    输入: s = "cab", t = "ad"
    输出: false
    解释: 无法通过 1 步操作使 s 变为 t。

    示例 3:
    输入: s = "1203", t = "1213"
    输出: true
    解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。

"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s == len_t:
            cnt = 0
            for i in range(len_s):
                if s[i] != t[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt > 0
        if len_s < len_t:
            len_s, len_t, s, t = len_t, len_s, t, s
        if len_s == len_t + 1:
            cs, ct, cnt = 0, 0, 0
            while cs < len_s and ct < len_t:
                if s[cs] != t[ct]:
                    cnt += 1
                    cs += 1
                    if cnt > 1:
                        return False
                else:
                    cs += 1
                    ct += 1
            return (cs == len_s and ct == len_t) or (cnt == 0)
        return False
