# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-11 14:31
 @Author  : QDY
 @FileName: 1616. 分割两个字符串得到回文串.py
 @Software: PyCharm
"""
"""
给你两个字符串a 和b，它们长度相同。请你选择一个下标，将两个字符串都在相同的下标 分割开。
由a可以得到两个字符串：aprefix和asuffix，满足a = aprefix + asuffix，
同理，由b 可以得到两个字符串bprefix 和bsuffix，满足b = bprefix + bsuffix。
请你判断aprefix + bsuffix 或者bprefix + asuffix能否构成回文串。

当你将一个字符串s分割成sprefix 和ssuffix时，ssuffix 或者sprefix 可以为空。
比方说，s = "abc"那么"" + "abc"，"a" + "bc"，"ab" + "c"和"abc" + ""都是合法分割。

如果 能构成回文字符串 ，那么请返回true，否则返回false。

请注意，x + y表示连接字符串x 和y。

示例 1：
输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。

输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。

提示：
1 <= a.length, b.length <= 105
a.length == b.length
a 和b都只包含小写英文字母

"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]

        if isPalindrome(a) or isPalindrome(b): return True

        def helper(a, b):
            n = len(a)
            l, r = 0, n - 1
            while l < r and a[l] == b[r]:  # 一个向后遍历，一个向前遍历
                l += 1
                r -= 1
            # 当a[l]!=a[r]时，若中间的字符串a[l:r+1]或b[l:r+1]是回文，则可组合成回文
            if isPalindrome(a[l:r + 1]) or isPalindrome(b[l:r + 1]):
                return True
            return False

        return helper(a, b) or helper(b, a)
