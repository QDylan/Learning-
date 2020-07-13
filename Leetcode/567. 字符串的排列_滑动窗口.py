# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/13 14:36
 @Author  : QDY
 @FileName: 567. 字符串的排列_滑动窗口.py

    给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
    换句话说，第一个字符串的排列之一是第二个字符串的子串。

    示例1:
    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").

    示例2:
    输入: s1= "ab" s2 = "eidboaoo"
    输出: False
     
    注意：
    输入的字符串只包含小写字母
    两个字符串的长度都在 [1, 10,000] 之间

"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if not s1: return True
        if len1 > len2: return False

        # 滑动窗口
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len1):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1

        cnt = 0  # 记录有多少种字符已经匹配成功
        for i in range(26):
            if count1[i] == count2[i]:
                cnt += 1
        # if count1 == count2:
        if cnt == 26:
            return True

        for i in range(len1, len2):
            if count2[ord(s2[i]) - 97] == count1[ord(s2[i]) - 97]:
                cnt -= 1  # 若之前是已匹配好的，则现在不再匹配了，cnt-1
            elif count2[ord(s2[i]) - 97] + 1 == count1[ord(s2[i]) - 97]:
                cnt += 1  #
            count2[ord(s2[i]) - 97] += 1

            if count2[ord(s2[i - len1]) - 97] == count1[ord(s2[i - len1]) - 97]:
                cnt -= 1
            elif count2[ord(s2[i - len1]) - 97] == count1[ord(s2[i - len1]) - 97] + 1:
                cnt += 1
            count2[ord(s2[i - len1]) - 97] -= 1
            # if count1 == count2:
            if cnt == 26:
                return True
        return False

        # c = Counter(s1)
        # window = Counter(s2[:len1])
        # if c==window:
        #     return True
        # for i in range(len1,len2):
        #     if s2[i] not in window:
        #         window[s2[i]] = 1
        #     else:
        #         window[s2[i]] += 1
        #     window[s2[i-len1]] -= 1
        #     if window[s2[i-len1]] == 0:
        #         window.pop(s2[i-len1])
        #     if window == c:
        #         return True
        # return False
