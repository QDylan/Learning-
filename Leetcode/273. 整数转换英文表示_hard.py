# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/21 14:48
 @Author  : QDY
 @FileName: 273. 整数转换英文表示_hard.py
 @Software: PyCharm
"""
"""
将非负整数转换为其对应的英文表示。可以保证给定输入小于 2**31 - 1 。

示例 1:
输入: 123
输出: "One Hundred Twenty Three"

示例 2:
输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"

示例 3:
输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

示例 4:
输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    def numberToWords(self, num: int) -> str:

        to19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ["Twenty", 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def helper(num):  # 递归
            if num < 20:  # [0,20)中的数，直接返回，0的话，to19[-1:0]返回空数组
                return to19[num - 1:num]
            if num < 100:  # [20,100)中的数，确定其十位数num//10，个位数num%10
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:  # [100,1000),确定其百位数num//100，余数num%100,
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):  # [1000,2**31-1]，p从1~3
                if num < 1000 ** (p + 1):  # 确定其最大的千进制符号p
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return " ".join(helper(num)) or "Zero"
