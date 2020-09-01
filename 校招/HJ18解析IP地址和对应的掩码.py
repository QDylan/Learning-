# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 17:48
 @Author  : QDY
 @FileName: HJ18解析IP地址和对应的掩码.py
 @Software: PyCharm
"""
"""题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
1
示例1
输入
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出

1 0 1 0 0 2 1
"""
import sys

res = [0, 0, 0, 0, 0, 0, 0]
ones = ['254', '252', '248', '240', '224', '192', '128', '0']


def check_code(code):  #检测掩码是否合法
    if len(code) != 4 or '' in code: return False
    if code[0] == '0' or code[-1] == '255': return False
    zero = False
    for num in code:
        if not zero:
            if num == '255':
                continue
            elif num in ones:
                zero = True
            else:
                return False
        else:
            if num != '0': return False

    return True


def check_ip(ip):  # 检测ip地址是否合法
    if len(ip) != 4: return False
    for num in ip:
        if not num.isdigit(): return False
        num = int(num)
        if num > 255 or num < 0: return False
    return True


while True:
    try:
        strs = sys.stdin.readline().strip()
        if strs == '': break
        ip, code = strs.split('~')
        ip = ip.split('.')
        code = code.split('.')
        if not check_code(code):
            res[5] += 1
        else:
            if check_ip(ip):
                first = int(ip[0])
                if 1 <= first <= 126:
                    res[0] += 1
                elif 128 <= first <= 191:
                    res[1] += 1
                elif 192 <= first <= 223:
                    res[2] += 1
                elif 224 <= first <= 239:
                    res[3] += 1
                elif 240 <= first <= 255:
                    res[4] += 1
                if first == 10 or (first == 172 and 16 <= int(ip[1]) <= 31) or (first == 192 and int(ip[1]) == 168):
                    res[6] += 1
            else:
                res[5] += 1
    except:
        break

res = [str(i) for i in res]
print(' '.join(res))
