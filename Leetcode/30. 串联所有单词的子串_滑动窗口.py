# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/13 10:30
 @Author  : QDY
 @FileName: 30. 串联所有单词的子串_滑动窗口.py

    给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

    示例 1：
    输入：
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    输出：[0,9]

    解释：
    从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
    输出的顺序不重要, [9,0] 也是有效答案。

    示例 2：
    输入：
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    输出：[]

"""
from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        if not s or not words: return []
        len_w = len(words[0])  # 每个单词的长度
        w_num = len(words)  # 单词的数量
        len_s = len(s)
        if len_s < w_num * len_w: return []

        words = Counter(words)  # 记录每个word的出现次数
        res = []
        for i in range(len_w):  # 维护一个长度为len_s的滑动窗口
            cnt = 0  # 记录窗口中的单词数
            left, right = i, i  # 窗口的左、右边界
            cur_Counter = Counter()  # 记录当前窗口每个word的出现次数
            while right + len_w <= len_s:  # 能向右扩展右边界
                w = s[right:right + len_w]  # 扩展下一个单词
                right += len_w
                if w not in words:  # 下个单词不在words中，重新开始寻找
                    left = right  # 重置左边界
                    cur_Counter.clear()
                    cnt = 0
                else:  # 下个单词可以加入窗口
                    cur_Counter[w] += 1
                    cnt += 1
                    while cur_Counter[w] > words[w]:  # 下个单词次数超了
                        left_w = s[left:left + len_w]  # 移动左边界
                        left += len_w
                        cur_Counter[left_w] -= 1  # 从左边界每次减去一个单词
                        cnt -= 1  # 直到减去一个w单词为止，才是合法的窗口
                    if cnt == w_num:
                        res.append(left)
        return res
