# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/3 10:06
 @Author  : QDY
 @FileName: 679. 24 点游戏.py
 @Software: PyCharm
"""
"""
    你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

    示例 1:
    输入: [4, 1, 8, 7]
    输出: True
    解释: (8-4) * (7-1) = 24

    示例 2:
    输入: [1, 2, 1, 2]
    输出: False

    注意:
    除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
    每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
    你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

"""


class Solution:
    def judgePoint24(self, nums) -> bool:
        self.res = False

        def dfs(cur):
            if self.res:
                return
            if len(cur) == 1:  # 当只剩一个数时，判断其是否是24的近似
                if abs(cur[0] - 24) < 0.0001:
                    self.res = True
                    return
            n = len(cur)
            for i in range(n - 1):  # 每次取出两个数做+-*/,再将结果放入
                for j in range(i + 1, n):
                    nxt = cur.copy()
                    num1 = nxt.pop(j)
                    num2 = nxt.pop(i)
                    dfs([num1 + num2] + nxt)
                    dfs([num1 * num2] + nxt)
                    dfs([num1 - num2] + nxt)
                    dfs([num2 - num1] + nxt)
                    if num2 != 0:
                        dfs([num1 / num2] + nxt)
                    if num1 != 0:
                        dfs([num2 / num1] + nxt)

        dfs(nums)
        return self.res
