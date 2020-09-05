# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-05 16:20
 @Author  : QDY
 @FileName: 6. Z 字形变换.py
 @Software: PyCharm
"""
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING"行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例2:
输入: s = "LEETCODEISHIRING", numRows =4
输出:"LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G

"""


class Solution:
    def convert(self, s, numRows):
        length = len(s)
        if length <= numRows or numRows < 2:
            return s

        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag  # flag 代表行索引变化的方向 即 是减小还是增加
            i += flag
        return ''.join(res)


if __name__ == '__main__':
    s = input()
    numRows = int(input())
    res = ['' for _ in range(numRows)]
    i, down = 0, 1
    for c in s:
        res[i] += c
        if down < 0 and i != 0:
            for j in range(numRows):
                if j != i: res[j] += ' '
        i += down
        if i == numRows:
            down = -1
            i = numRows - 2
        elif i < 0:
            down = 1
            i = 1
    for strs in res:
        print(strs)
    # print(res)
