# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-13 17:01
 @Author  : QDY
 @FileName: 5514. 检查字符串是否可以通过排序子字符串得到另一个字符串.py
 @Software: PyCharm
"""
"""
给你两个字符串s 和t，请你通过若干次以下操作将字符串s转化成字符串t：

选择 s中一个 非空子字符串并将它包含的字符就地 升序排序。
比方说，对下划线所示的子字符串进行操作可以由"14234"得到"12344"。
如果可以将字符串 s变成 t，返回 true。否则，返回 false。
一个 子字符串定义为一个字符串中连续的若干字符。

示例 1：
输入：s = "84532", t = "34852"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"84532" （从下标 2 到下标 3）-> "84352"
"84352" （从下标 0 到下标 2） -> "34852"

示例 2：
输入：s = "34521", t = "23415"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"34521" -> "23451"
"23451" -> "23415"

示例 3：
输入：s = "12345", t = "12435"
输出：false

示例 4：
输入：s = "1", t = "2"
输出：false

提示：
s.length == t.length
1 <= s.length <= 105
s 和t都只包含数字字符，即'0'到'9' 。

"""
from collections import defaultdict, deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        pos = defaultdict(deque)
        for i in range(n):  # 记录s每个数字出现的位置
            pos[int(s[i])].append(i)
        for i in range(n):  # 遍历字符串t
            digit = int(t[i])
            if not pos[digit]: return False  # s中无digit或数量不够
            for j in range(digit):  # 遍历每个比digit小的字符
                if pos[j] and pos[j][0] < pos[digit][0]:
                    return False  # 剩余的s中存在一个可用的j比digit的位置靠前，则怎样都无法把digit换到j前面去
            pos[digit].popleft()  # digit可以放在位置i上
        return True
