# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/13 16:27
 @Author  : QDY
 @FileName: 93. 复原IP地址.py

    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

    示例:
    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]

"""


class Solution:
    def restoreIpAddresses(self, s):
        self.res, len_s = [], len(s)
        if len_s < 4 or len_s > 12: return []

        # dfs
        def search_ip(i, cnt, tmp):  # 在s[i:]中寻找cnt个合法的ip整数
            if cnt == 1:  # cnt为1时，剩下的字符s[i:]作为最后一个ip整数，判断其是否合法
                num = int(s[i:])  # 超过255是非法的，除了'0'之外由'0'开头的数也是非法的
                if not (num > 255 or (len_s - i > 1 and s[i] == '0')):
                    self.res.append('.'.join(tmp + [s[i:]]))
                return
            if len_s - i < cnt or len_s - i > 3 * cnt:  # 剪枝
                return  # 当剩余地址长度不足cnt或超过了3*cnt，则一定无法选出cnt个合法的ip整数
            for j in range(3):  # 下一个ip整数为s[i:i+j+1]
                if j + i == len_s - 1:  # 若下一个整数用完了全部地址，则无法继续寻找再下一个整数，
                    break  # 说明这个整数的长度不合适，直接跳出
                num = int(s[i:i + j + 1])
                if not (num > 255 or (j + 1 > 1 and s[i] == '0')):
                    search_ip(i + j + 1, cnt - 1, tmp + [s[i:i + j + 1]])

        for j in range(3):
            if len_s - j < 4:
                break
            num = int(s[:j + 1])  # 找到第一个合法的ip整数
            if not (num > 255 or (j + 1 > 1 and s[0] == '0')):
                search_ip(j + 1, 3, [s[:j + 1]])

        return self.res
