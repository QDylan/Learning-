# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/4 14:10
 @Author  : QDY
 @FileName: 68. 文本左右对齐.py
 @Software: PyCharm
"""
"""
    给定一个单词数组和一个长度maxWidth，重新排版单词，使其成为每行恰好有maxWidth个字符，且左右两端对齐的文本。
    你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格' '填充，使得每行恰好有 maxWidth个字符。
    要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
    文本的最后一行应为左对齐，且单词之间不插入额外的空格。

    说明:

    单词是指由非空格字符组成的字符序列。
    每个单词的长度大于 0，小于等于maxWidth。
    输入单词数组 words至少包含一个单词。
    示例:
    输入:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    输出:
    [
    "This is an",
    "example of text",
    "justification. "
    ]

    示例2:
    输入:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    输出:
    [
    "What must be",
    "acknowledgment ",
    "shall be "
    ]
    解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
        因为最后一行应为左对齐，而不是左右两端对齐。       
        第二行同样为左对齐，这是因为这行只包含一个单词。

    示例3:
    输入:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
            "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    输出:
    [
     "Science is what we",
    "understand  well",
     enough to explain to",
    "a computer. Art is",
     "everything else we",
     "do "
    ]

"""


class Solution:
    def fullJustify(self, words, maxWidth: int):
        res, tmp, cur_len = [], [words[0]], len(words[0])
        for i in range(1, len(words)):

            if cur_len + len(words[i]) + 1 <= maxWidth:
                tmp.append(words[i])
                cur_len += len(words[i]) + 1
            else:
                if len(tmp) > 1:  # 若超过一个单词，则需要两端对齐
                    rest = maxWidth - cur_len
                    average = rest // (len(tmp) - 1)
                    rest -= average * (len(tmp) - 1)
                    for j in range(len(tmp) - 1):  # 均匀分配空格
                        tmp[j] += ' ' * average
                        if rest > 0:
                            tmp[j] += ' '
                            rest -= 1
                    res.append(' '.join(tmp))
                else:  # 只有一个单词，左对齐即可
                    res.append(tmp[0] + ' ' * (maxWidth - cur_len))
                tmp = [words[i]]
                cur_len = len(words[i])
            # print(i,tmp)

        res.append(' '.join(tmp) + ' ' * (maxWidth - cur_len))  # 最后一句左对齐

        return res
