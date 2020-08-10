# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/9 23:27
 @Author  : QDY
 @FileName: 5485. 找出最长的超赞子字符串.py
 @Software: PyCharm
"""

"""
    给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
    「超赞子字符串」需满足满足下述两个条件：

    该字符串是 s 的一个非空子字符串
    进行任意次数的字符交换重新排序后，该字符串可以变成一个回文字符串
     
    示例 1：
    输入：s = "3242415"
    输出：5
    解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"

    示例 2：
    输入：s = "12345678"
    输出：1

    示例 3：
    输入：s = "213123"
    输出：6
    解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"

    示例 4：
    输入：s = "00"
    输出：2

    提示：
    1 <= s.length <= 10^5
    s 仅由数字组成

"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        status = {0: -1}  # 记录每个状态的最早出现位置
        res, cur = 0, 0  # 状态压缩
        for i in range(len(s)):
            num = int(s[i])  # 计算前缀s[:i+1]每个数字的奇偶状态
            cur ^= 1 << num  # cur的从右数第num+1个数改变奇偶状态
            for j in range(10):  # 0~9
                if cur ^ (1 << j) in status:  # 若之前出现过只与cur有一位不同的状态
                    # 则 s[cur ^ (1<<j)+1:i+1]之中，只有这一个不同状态的数出现了奇数次
                    res = max(res, i - status[cur ^ (1 << j)])
            if cur in status:  # 若当前状态cur出现过，则s[status[cur]+1:i+1]之中没有出现奇数次的数字
                res = max(res, i - status[cur])
            else:
                status[cur] = i
        return res
