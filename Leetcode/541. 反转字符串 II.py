# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-30 10:29
 @Author  : QDY
 @FileName: 541. 反转字符串 II.py
 @Software: PyCharm
"""
"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。

"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k  # 初始化左中右指针
        res = ''  # 初始化结果字符串
        while len(res) < len(s):  # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]  # 把当前单元的结果添加到结果字符串
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
        return res  # 返回结果
