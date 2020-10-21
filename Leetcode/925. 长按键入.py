# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-21 9:38
 @Author  : QDY
 @FileName: 925. 长按键入.py
 @Software: PyCharm
"""
"""
你的朋友正在使用键盘输入他的名字name。偶尔，在键入字符c时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回True。

示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

提示：
name.length <= 1000
typed.length <= 1000
name 和typed的字符都是小写字母。

"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        N, T = len(name), len(typed)
        while j < T:
            if i < N and name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and typed[j] == name[i - 1]:
                j += 1
            else:
                return False
        return i == N
