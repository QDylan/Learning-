# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/28 10:10
 @Author  : QDY
 @FileName: 650. 只有两个键的键盘.py
 @Software: PyCharm
"""
"""
    最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
    Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
    Paste (粘贴) : 你可以粘贴你上一次复制的字符。
    给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。

    示例 1:
    输入: 3
    输出: 3
    解释:
    最初, 我们只有一个字符 'A'。
    第 1 步, 我们使用 Copy All 操作。
    第 2 步, 我们使用 Paste 操作来获得 'AA'。
    第 3 步, 我们使用 Paste 操作来获得 'AAA'。

"""


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        res, i = 0, 2
        while i <= n:  # 分解质因数
            while n % i == 0:
                res += i
                n //= i
            i += 1
        return res
        # factor, i = 1, 2
        # while i<=n**0.5:
        #     if n % i == 0:
        #         factor = i
        #         break
        #     i += 1
        # if factor == 1:return n
        # return max_factor + self.minSteps(n//factor)
