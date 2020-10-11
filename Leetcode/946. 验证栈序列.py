# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-11 14:54
 @Author  : QDY
 @FileName: 946. 验证栈序列.py
 @Software: PyCharm
"""
"""
给定pushed和popped两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

提示：
0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed是popped的排列。

"""


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        N, j, stack = len(popped), 0, []
        for x in pushed:  # 模拟进栈出栈
            stack.append(x)
            while stack and j < N and stack[-1] == popped[j]:  # 判断是否需要出栈
                stack.pop()
                j += 1

        return j == N
