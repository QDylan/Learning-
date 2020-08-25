# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/25 9:45
 @Author  : QDY
 @FileName: 763. 划分字母区间.py
 @Software: PyCharm
"""
"""
    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

    示例 1：
    输入：S = "ababcbacadefegdehijhklij"
    输出：[9,7,8]
    解释：
    划分结果为 "ababcbaca", "defegde", "hijhklij"。
    每个字母最多出现在一个片段中。
    像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
     
    提示：
    S的长度在[1, 500]之间。
    S只包含小写字母 'a' 到 'z' 。

"""


class Solution:
    def partitionLabels(self, S: str):
        pos, res = {}, []
        for i, c in enumerate(S):
            pos[c] = i  # 记录每种字符的最右位置
        i, length = 0, len(S)
        while i < length:
            left, right = i, pos[S[i]]  # 查找当前片段的右边界
            while i < right:
                right = max(pos[S[i]], right)
                i += 1
            res.append(right - left + 1)
            i += 1
        return res
