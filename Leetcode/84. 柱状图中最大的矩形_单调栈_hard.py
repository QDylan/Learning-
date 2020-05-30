# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/30 10:08
 @Author  : QDY
 @FileName: 84. 柱状图中最大的矩形_单调栈_hard.py

    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。

    示例:
    输入: [2,1,5,6,2,3]
    输出: 10
"""


class Solution:
    def largestRectangleArea(self, heights):
        if not heights: return 0
        heights.append(0)
        stack = [0]  # 单调栈,按高度单调递增，记录坐标
        res = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:  # 一旦发现当前高度小于栈顶高度，计算
                prev_h = heights[stack.pop()]  # 弹出栈顶坐标的高度,直到栈顶坐标小于等于heights[i]
                width = i - 1 - stack[-1] if stack else i
                res = max(res, width * prev_h)
            stack.append(i)
        return res
