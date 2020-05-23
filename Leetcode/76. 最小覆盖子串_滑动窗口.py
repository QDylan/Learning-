# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/23 22:12
 @Author  : QDY
 @FileName: 76. 最小覆盖子串_滑动窗口.py

    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

    示例：
    输入: S = "ADOBECODEBANC", T = "ABC"
    输出: "BANC"
    说明：

    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。

"""
class Solution:
    def minWindow(self, s, t):
        len_s, len_t = len(s), len(t)
        if len_s<len_t:return ''

        hp,hp_tmp = {},{}
        for i in t:
            if i not in hp:
                hp[i] = 1
            else:
                hp[i] += 1
        len_hp = len(hp)


        start = 0
        while start<len_s and s[start] not in hp:
            start += 1
        if start+len_t > len_s: return ''

        res_len = float('inf')
        res = ''
        i = start
        cnt = 1
        while i < len_s:
            while i < len_s:  # 窗口不包含t,在窗口右侧添加字符
                if s[i] in hp:
                    hp[s[i]] -= 1
                    if hp[s[i]]<=0:
                        hp_tmp[s[i]] = 1
                        # print('right+',s[start:i+1],hp)
                        if len(hp_tmp)==len_hp:  # 找到了包含t所有字符的字串
                            if i-start+1<res_len:
                                res_len = i-start+1
                                res = s[start:i+1]
                                # print('res',res,hp,hp_tmp)
                            break

                i += 1

            j = start
            # print(hp_tmp,hp)
            while res_len!=float('inf') and len(hp_tmp)==len_hp and j<len_s:  # 在左侧减少字符
                if s[j] in hp:
                    hp[s[j]] += 1
                    # print(hp)
                    if hp[s[j]] > 0:  # 窗口已不包含t的所有字符

                        hp_tmp.pop(s[j])
                        start = j+1
                        i += 1
                        # print('',s[j+1:i],hp,hp_tmp)
                        break  # 跳出，在右侧添加字符
                    else: # 窗口仍包含t的所有字符
                        # print(i,j)
                        if i-j < res_len:
                            res_len = i-j
                            res = s[j+1:i+1]
                        # print('left--',s[j+1:i+1],hp,hp_tmp)

                else:
                    if i-j < res_len:
                        res_len = i-j
                        res = s[j+1:i+1]
                    # print('left-',s[j+1:i+1],hp,hp_tmp)
                j += 1

        return res