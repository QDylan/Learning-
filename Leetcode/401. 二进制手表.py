# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-06 10:32
 @Author  : QDY
 @FileName: 401. 二进制手表.py
 @Software: PyCharm
"""
"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。

例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n代表当前 LED 亮着的数量，返回所有可能的时间。


示例：
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

提示：
输出的顺序没有要求。
小时不会以零开头，比如 “01:00”是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2”是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

"""


class Solution:
    def readBinaryWatch(self, num: int):
        if not num: return ['0:00']
        hours, mins = [1, 2, 4, 8], [1, 2, 4, 8, 16, 32]
        tmp_h, tmp_m = [], []

        def dfs_h(i, cnt, cur):
            if cnt == 0:
                tmp_h.append(str(cur))
                return
            for j in range(i, 4 - cnt + 1):
                nxt = cur + hours[j]
                if nxt > 11: break
                dfs_h(j + 1, cnt - 1, nxt)

        def dfs_m(i, cnt, cur):
            if cnt == 0:
                if cur >= 10:
                    tmp_m.append(str(cur))
                else:
                    tmp_m.append('0' + str(cur))
                return
            for j in range(i, 6 - cnt + 1):
                nxt = cur + mins[j]
                if nxt >= 60: break
                dfs_m(j + 1, cnt - 1, nxt)

        res = []
        for h in range(4):
            if h > num: break
            m = num - h
            if m >= 6: continue
            tmp_h, tmp_m = [], []
            dfs_h(0, h, 0)
            dfs_m(0, m, 0)

            for hh in tmp_h:
                for mm in tmp_m:
                    res.append('%s:%s' % (hh, mm))
        return res
