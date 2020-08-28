# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/7 10:27
 @Author  : QDY
 @FileName: 85. 最大矩形.py
 @Software: PyCharm
"""
"""
    给定一个仅包含0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

    示例:
    输入:
    [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
    输出: 6

"""


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        h, w = len(matrix), len(matrix[0])
        # 单调栈 找柱状图中最大的矩形 O(MN)
        res, stack, cur_h = 0, [0] * w, [0] * (w + 1)  # cur_h末尾多增一个0，方便处理一直递增到右边界的情况
        for j in range(w):  # 对第一行处理
            if matrix[0][j] == '1':
                cur_h[j] = 1
                stack[j] = 1 + stack[j - 1]
                res = max(stack[j], res)

        for i in range(1, h):
            stack = []  # 维护一个柱高度单调递增的栈
            for j in range(w + 1):
                if j == w or matrix[i][j] == '0':  # 遇到0,矩形中断, 高度为0
                    cur_h[j] = 0
                else:  # 遇到1
                    cur_h[j] += 1  # cur_h 为以matrix[i][j]为底的柱的高度
                while stack and cur_h[j] < cur_h[stack[-1]]:  # 当前高度小于栈顶柱高度
                    prev_h = cur_h[stack.pop()]  # 出栈,计算高度
                    cur_w = j - 1 - stack[-1] if stack else j  # 计算当前矩形宽度
                    res = max(res, cur_w * prev_h)
                stack.append(j)  # 将当前索引入栈
        return res

        # O(MN^2)
        # square = [[0]*w for i in range(h)]
        # for i in range(h):
        #     for j in range(w):
        #         if matrix[i][j] == '1':
        #             square[i][j] = square[i][j-1]+1
        # res = max(square[0])
        # for i in range(1,h):
        #     for j in range(w):
        #         if square[i][j] > 0:
        #             length = square[i][j]
        #             res = max(res,length)
        #             for k in range(i-1,-1,-1):
        #                 if square[k][j] == 0:
        #                     break
        #                 length = min(length,square[k][j])
        #                 res = max(res,length * (i-k+1))
        # return res
