# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/22 9:51
 @Author  : QDY
 @FileName: 面试题 16.18. 模式匹配.py

    你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，
    用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"
    （其中"cat"是"a"，"go"是"b"），
    该字符串也匹配像"a"、"ab"和"b"这样的模式。
    但需注意"a"和"b"不能同时表示相同的字符串。
    编写一个方法判断value字符串是否匹配pattern字符串。

    示例 1：
    输入： pattern = "abba", value = "dogcatcatdog"
    输出： true

    示例 2：
    输入： pattern = "abba", value = "dogcatcatfish"
    输出： false

    示例 3：
    输入： pattern = "aaaa", value = "dogcatcatdog"
    输出： false

    示例 4：
    输入： pattern = "abba", value = "dogdogdogdog"
    输出： true
    解释： "a"="dogdog",b=""，反之也符合规则

    提示：
    0 <= len(pattern) <= 1000
    0 <= len(value) <= 1000
    你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

"""


class Solution:
    def patternMatching(self, pattern, value):
        if not pattern: return not value  # p为空时，只有v也为空才能匹配
        len_p, len_v = len(pattern), len(value)
        cnt_a = pattern.count('a')
        cnt_b = len_p - cnt_a
        if not value:  # v为空时，需要只有一种字符，该字符表示为空，才能匹配
            return cnt_a == 0 or cnt_b == 0

        if cnt_a < cnt_b:  # 令a是出现较多的
            cnt_a, cnt_b = cnt_b, cnt_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if cnt_b == 0:  # 若只有一种字符
            if len_v % cnt_a != 0: return False  # 若不能整除，说明v不可能分为cnt_a个单词
            len_a = len_v // cnt_a  # 可以确定每个词的长度
            for i in range(cnt_a):  # 逐段匹配是否都相等
                if value[i * len_a:i * len_a + len_a] != value[0:len_a]:
                    return False
            return True

        for len_a in range(len_v // cnt_a + 1):  # 枚举a,最大长度小于len_v // cnt_a + 1
            if (len_v - len_a * cnt_a) % cnt_b != 0:  # 剩余的字符串长度不能被cnt_b整除，说明不可能存在len_a的划分
                continue
            else:
                len_b = (len_v - len_a * cnt_a) // cnt_b  # 可以计算出b的长度，保证能匹配完v中所有字符
                pos, check = 0, True  # pos为当前v的位置
                a, b = None, None
                for char in pattern:  # 遍历p中的每个字符
                    if char == 'a':
                        sub = value[pos:pos + len_a]
                        if a is None:  # 第一次遇到a,给a赋值
                            a = sub
                        elif a != sub:  # 若当前字符不等于a，说明匹配失败
                            check = False
                            break
                        pos += len_a  # 移动v中pos的位置
                    else:
                        sub = value[pos:pos + len_b]
                        if b is None:
                            b = sub
                        elif b != sub:
                            check = False
                            break
                        pos += len_b
                if check and a != b:  # 当匹配完p中所有字符后，检查check和单词a、b是否不相等
                    # print(a,b)
                    return True
        return False
