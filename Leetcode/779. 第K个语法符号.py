# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/20 10:51
 @Author  : QDY
 @FileName: 779. 第K个语法符号.py

    在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
    给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）

    例子:
    输入: N = 1, K = 1
    输出: 0
    输入: N = 2, K = 1
    输出: 0
    输入: N = 2, K = 2
    输出: 1
    输入: N = 4, K = 5
    输出: 1

    解释:
    第一行: 0
    第二行: 01
    第三行: 0110
    第四行: 01101001

    注意：
    N 的范围 [1, 30].
    K 的范围 [1, 2^(N-1)].

"""


class Solution:
    def kthGrammar(self, N, K):
        """
                     1
                /         \
              1              2
            /   \          /    \
          1       2       3       4
        / \     /  \     /  \    / \
        1   2   3    4   5    6  7   8

        01排列
                      0
                 /         \
              0              1
            /   \          /    \
          0       1       1       0
        /  \     /  \    /  \    /  \
        0   1   1    0  1    0  0    1
        """

        if N == 1 and K == 1:
            return 0
        root = self.kthGrammar(N - 1, (K + 1) // 2)
        if K & 1:  # K为奇数，与父节点相同
            return root
        else:  # K为偶数，与父节点相反
            return root ^ 1
