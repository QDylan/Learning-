# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/20 9:47
 @Author  : QDY
 @FileName: 1371. 每个元音包含偶数次的最长子字符串_前缀和+状态压缩.py

    给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，
    即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

    示例 1：
    输入：s = "eleetminicoworoep"
    输出：13
    解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。

    示例 2：
    输入：s = "leetcodeisgreat"
    输出：5
    解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。

    示例 3：
    输入：s = "bcbcbc"
    输出：6
    解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
     

    提示：
    1 <= s.length <= 5 x 10^5
    s 只包含小写英文字母。

"""


class Solution:
    def findTheLongestSubstring(self, s):
        res = 0
        vowels = 0  # 二进制数 00000，每个位置上分别表示元音字母aeiou的奇偶,共32种奇偶组合
        pos = [-1] * (1 << 5)  # pos[i]为第一次出现第i种奇偶组合时的结束位置，即s[:pos[i]]的奇偶组合为i
        pos[0] = 0
        tmp = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        for i in range(len(s)):
            if s[i] in tmp:
                vowels ^= 1 << tmp[s[i]]

            if ~pos[vowels]:  # pos[vowels]!=-1, 说明之前s[:pos[vowels]+1]的元音字母状态也为vowels
                res = max(res, i + 1 - pos[vowels])  # s[pos[vowels]:i+1]一定每个元音字母都出现了偶数次
            else:  # 之前没有出现过该种奇偶组合vowels,记录节点
                pos[vowels] = i + 1

        return res
