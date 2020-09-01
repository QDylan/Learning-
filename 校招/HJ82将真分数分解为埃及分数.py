# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 21:14
 @Author  : QDY
 @FileName: HJ82将真分数分解为埃及分数.py
 @Software: PyCharm
"""
"""
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。


接口说明

/*
功能: 将分数分解为埃及分数序列
输入参数：
String pcRealFraction:真分数(格式“8/11”)
返回值：
String pcEgpytFraction:分解后的埃及分数序列(格式“1/2+1/5+1/55+1/100”)
*/

public static String  ConvertRealFractToEgpytFract(String pcRealFraction)
{
return null;
}

如有多个解，输出任意一个



输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string

示例1
输入
8/11
输出
1/2+1/5+1/55+1/110
"""
while True:
    try:
        A, B = map(int, input().split('/'))
        res = []
        while A != 1:
            if B % A == 0:  # A整除B时直接约分
                B = B // A
                break
            # 带余除法 B=q*A+r,r<A  --> B-r=q*A
            # 则 A/B = A*(q+1)/(B*(q+1)) = (q*A+A)/(B*(q+1)) = (B-r+A)/(B*(q+1))
            #       = B/(B*(q+1)) + (A-r)/(B*(q+1)) = 1/(q+1)+(A-r)/(B*(q+1))
            q = B // A
            r = B % A
            res.append('1/%s' % (q + 1))
            print()
            A, B = A - r, B * (q + 1)
        res.append('1/%s' % B)
        print('+'.join(res))
    except:
        break
