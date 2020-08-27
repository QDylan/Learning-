# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/27 14:12
 @Author  : QDY
 @FileName: 753. 破解保险箱.py
 @Software: PyCharm
"""
"""
    有一个需要密码才能打开的保险箱。密码是n 位数, 密码的每一位是k位序列0, 1, ..., k-1中的一个 。
    你可以随意输入密码，保险箱会自动记住最后n位输入，如果匹配，则能够打开保险箱。
    举个例子，假设密码是"345"，你可以输入"012345"来打开它，只是你输入了 6个字符.
    请返回一个能打开保险箱的最短字符串。


    示例1:
    输入: n = 1, k = 2
    输出: "01"
    说明: "10"也可以打开保险箱。
    
    示例2:
    输入: n = 2, k = 2
    输出: "00110"
    说明: "01100", "10011", "11001" 也能打开保险箱。
    
    提示：
    n 的范围是[1, 4]。
    k 的范围是[1, 10]。
    k^n 最大可能为4096。

"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        char = list(map(str, range(k)))
        used = set()
        self.res = ''

        def dfs(cur):
            for x in char:
                nxt = cur + x
                if nxt not in used:  # 当前字段密码尚未出现
                    used.add(nxt)
                    dfs(nxt[1:])
                    self.res += x

        dfs('0' * (n - 1))
        return self.res + '0' * (n - 1)
