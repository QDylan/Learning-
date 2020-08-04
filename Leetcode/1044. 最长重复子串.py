# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/4 11:40
 @Author  : QDY
 @FileName: 1044. 最长重复子串.py
 @Software: PyCharm
"""
"""
    给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
    返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）

    示例 1：
    输入："banana"
    输出："ana"

    示例 2：
    输入："abcd"
    输出：""
     
    提示：
    2 <= S.length <= 10^5
    S 由小写英文字母组成。

"""


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(i) - 97 for i in S]
        modulus = 2 ** 32

        def search(l):  # 搜索长度为l的字符串
            # Rabin-Karp字符串编码
            # 'abde' ->[0,1,3,4] -> 0*26^3+1*26^2+3*26^1+4*26^0
            h = 0
            for i in range(l):  # 计算第一个窗口的hash
                h = (h * 26 + nums[i]) % modulus
            visited = {h}
            first = (26 ** l) % modulus
            for i in range(l, n):
                h = (h * 26 - nums[i - l] * first + nums[i]) % modulus
                if h in visited:
                    return i - l + 1
                visited.add(h)
            return -1  # 没找到

        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if search(mid) == -1:
                right = mid
            else:
                left = mid + 1
        start = search(left - 1)
        return '' if start == -1 else S[start:start + left - 1]
