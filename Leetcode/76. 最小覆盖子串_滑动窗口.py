# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/23 22:12
 @Author  : QDY
 @FileName: 76. 最小覆盖子串_滑动窗口.py

    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

    示例：
    输入: S = "ADOBECODEBANC", T = "ABC"
    输出: "BANC"
    说明：

    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。

"""


class Solution:
    def minWindow(self, s, t):
        len_s, len_t = len(s), len(t)
        if len_s < len_t: return ''

        hp = {}  # 哈希表，存储t中的每个字符以及出现次数
        for i in t:
            if i not in hp:
                hp[i] = 1
            else:
                hp[i] += 1
        not_found = len(hp)  # 记录有多少种字符还不存在在窗口中

        start = 0
        while start < len_s and s[start] not in hp:  # 第一个窗口从第一个出现了t中的字符的位置开始
            start += 1

        res_len = float('inf')
        res = ''
        i = start
        while i < len_s:
            while i < len_s:  # 窗口不包含t,在窗口右侧添加字符
                if s[i] in hp:
                    hp[s[i]] -= 1
                    if hp[s[i]] <= 0:  # 若该字符的出现次数超过t中该字符的出现次数，则判断是否已找到全部字符
                        if hp[s[i]] == 0:  # 只有当该字符的次数刚好减为0时，才使not_found-1
                            not_found -= 1
                        if not_found == 0:  # 找到了包含t所有字符的字串
                            if i - start + 1 < res_len:
                                res_len = i - start + 1
                                res = s[start:i + 1]
                            break

                i += 1

            j = start
            while not not_found and j < len_s:  # 当找到了全部字符时，在左侧减少字符
                if s[j] in hp:  # 删除了一个t中的字符
                    hp[s[j]] += 1
                    if hp[s[j]] > 0:  # 窗口已不包含t的所有字符，判断删除前的字符串长度是不是最小
                        if i - j + 1 < res_len:
                            res_len = i - j + 1
                            res = s[j:i + 1]
                        not_found += 1  # 标记窗口为不再是找到了所有字符的状态
                        start = j + 1  # 新的窗口的起点
                        i += 1  # 新的搜索窗口的右边界的起点
                        break  # 跳出，转到在右侧添加字符
                j += 1

        return res
