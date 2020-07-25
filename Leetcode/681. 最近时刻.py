# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/25 12:13
 @Author  : QDY
 @FileName: 681. 最近时刻.py
 @Software: PyCharm
"""
"""
给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。


样例 1:
输入: "19:34"
输出: "19:39"
解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后。

样例 2:
输入: "23:59"
输出: "22:22"
解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。

"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def is_valid(t):  # 判断是否是有效的时间
            if t[0] * 10 + t[1] >= 24: return False
            if t[2] * 10 + t[3] >= 60: return False
            return True

        number, res = set(), []
        for s in time:
            if s.isdigit():
                number.add(int(s))
                res.append(int(s))
        number = sorted(list(number))
        for i in range(3, -1, -1):
            j = number.index(res[i])
            if j < len(number) - 1:
                res[i] = number[j + 1]
                # print(res,number,j)
                if is_valid(res):
                    return '%s%s:%s%s' % (res[0], res[1], res[2], res[3])
                else:
                    res[i] = number[0]
            else:
                res[i] = number[0]

        return '%s%s:%s%s' % (res[0], res[1], res[2], res[3])
