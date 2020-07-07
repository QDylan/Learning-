"""
 @Time    : 2020-07-07 23:11
 @Author  : QDY
 @FileName: 166. 分数到小数.py

    给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

    如果小数部分为循环小数，则将循环的部分括在括号内。

    示例 1:
    输入: numerator = 1, denominator = 2
    输出: "0.5"

    示例 2:
    输入: numerator = 2, denominator = 1
    输出: "2"

    示例 3:
    输入: numerator = 2, denominator = 3
    输出: "0.(6)"

"""


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sgn = 1
        if numerator < 0:
            sgn *= -1
            numerator = -numerator
        if denominator < 0:
            sgn *= -1
            denominator = -denominator
        if sgn < 0:
            head = '-'
        else:
            head = ''
        head += str(numerator // denominator) + '.'  # 整数部分
        # print(head)
        r = numerator % denominator
        pos = 0
        remainder = {}  # 记录余数出现的位置
        tmp = ''
        while True:
            tmp += str(r // denominator)  # 记录小数部分
            # print(tmp)
            r = r % denominator
            if r == 0:  # 不是循环小数
                return head + tmp[1:]
            if r in remainder:  #
                return '%s%s(%s)' % (head, tmp[1:remainder[r] + 1], tmp[remainder[r] + 1:pos + 1])
            else:
                remainder[r] = pos
            pos += 1
            r *= 10
