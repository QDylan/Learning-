# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-14 9:49
 @Author  : QDY
 @FileName: 1002. 查找常用字符.py
 @Software: PyCharm
"""
"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]

提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

"""
from collections import Counter


class Solution:
    def commonChars(self, A):
        cnters, res = [], []
        for word in A:
            cnters.append(Counter(word))
        for c in cnters[0]:
            valid = True
            min_cnt = cnters[0][c]
            for i in range(1, len(cnters)):
                if cnters[i][c] == 0:
                    valid = False
                    break
                else:
                    min_cnt = min(min_cnt, cnters[i][c])
                    cnters[i][c] -= min_cnt
            if valid:
                res += [c] * min_cnt
        return res
