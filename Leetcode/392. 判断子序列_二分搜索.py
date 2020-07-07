# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/9 18:42
 @Author  : QDY
 @FileName: 392. 判断子序列_二分搜索.py

    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
    （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    示例 1:
    s = "abc", t = "ahbgdc"
    返回 true.

    示例 2:
    s = "axc", t = "ahbgdc"
    返回 false.

"""
# class Solution:
#     def isSubsequence(self, s, t):
#         if not s:return True
#         if not t:return False

#         s_id,t_id = 0 ,0
#         len_s,len_t = len(s),len(t)
#         while s_id<len_s and t_id<len_t:
#             if s[s_id]==t[t_id]:
#                 s_id += 1
#                 t_id += 1
#             else:
#                 t_id += 1

#         return s_id==len_s

"""
后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。
在这种情况下，你会怎样改变代码？

"""


class Solution:
    def isSubsequence(self, s, t):
        if not s: return True
        if not t: return False

        len_t = len(t)
        index = {}  # 预处理，用一个字典index将每个字符出现的索引位置按顺序存储下来
        for i in range(len_t):  # 对于多个s的情况，可以将这一部分抽出来
            if t[i] not in index:
                index[t[i]] = [i]
            else:
                index[t[i]].append(i)

        # print(index)
        def find(id_, index_):  # 在有序index_列表中二分找出比id_大的最小元素(左侧边界查找)
            l, r = 0, len(index_) - 1
            while l <= r:
                m = l + (r - l) // 2
                if index_[m] < id_:
                    l = m + 1
                else:
                    r = m - 1
            return index_[l]

        i = 0
        for char in s:
            # print(i)index
            # index中无char 或 index[char]中没有比i大的元素
            if char not in index or i > index[char][-1]:
                return False
            else:
                i = find(i, index[char]) + 1
        return True
