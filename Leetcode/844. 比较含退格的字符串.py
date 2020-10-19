# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-19 9:43
 @Author  : QDY
 @FileName: 844. 比较含退格的字符串.py
 @Software: PyCharm
"""
"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

提示：
1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。

进阶：
你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # s, t = [], []
        # for i in S:
        #     if s and i == '#':
        #         s.pop()
        #     elif i != '#':
        #         s.append(i)
        # for i in T:
        #     if t and i == '#':
        #         t.pop()
        #     elif i != '#':
        #         t.append(i)
        # return ''.join(s) == ''.join(t)
        s, t = len(S) - 1, len(T) - 1
        skipS, skipT = 0, 0
        while s >= 0 or t >= 0:  # 双指针，从末端往前遍历
            while s >= 0:
                if S[s] == '#':
                    skipS += 1
                elif skipS > 0:
                    skipS -= 1
                else:
                    break
                s -= 1
            while t >= 0:
                if T[t] == '#':
                    skipT += 1
                elif skipT > 0:
                    skipT -= 1
                else:
                    break
                t -= 1
                # print(s,S[s],t,T[t])
            if s < 0 and t < 0:
                break
            elif s >= 0 and t >= 0 and S[s] == T[t]:
                s -= 1
                t -= 1
            else:
                return False
        return True
