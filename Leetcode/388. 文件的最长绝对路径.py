# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-02 10:56
 @Author  : QDY
 @FileName: 388. 文件的最长绝对路径.py
 @Software: PyCharm
"""
"""
假设我们以下述方式将我们的文件系统抽象成一个字符串:

字符串"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 表示:

dir
    subdir1
    subdir2
        file.ext
目录dir 包含一个空的子目录subdir1 和一个包含一个文件file.ext的子目录subdir2 。

字符串 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 表示:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
目录dir 包含两个子目录 subdir1 和subdir2。subdir1 包含一个文件file1.ext 和一个空的二级子目录 subsubdir1。
subdir2 包含一个二级子目录subsubdir2 ，其中包含一个文件file2.ext。

我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。
例如，在上述的第二个例子中，最长路径为"dir/subdir2/subsubdir2/file2.ext"，其长度为32 (不包含双引号)。
给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回0。

说明:
文件名至少存在一个. 和一个扩展名。
目录或者子目录的名字不能包含.。
要求时间复杂度为O(n)，其中n 是输入字符串的大小。

请注意，如果存在路径aaaaaaaaaaaaaaaaaaaaa/sth.png的话，那么a/aa/aaa/file1.txt就不是一个最长的路径。

"""


class Solution:
    def lengthLongestPath(self, strs: str) -> int:
        prefix, res = [0], 0
        for s in strs.split('\n'):  # \n 分割, s为一个文件夹或文件
            level = 0  # 当前层数
            while s[level] == '\t':  # 以\t开头，进入下一层目录
                level += 1
            len_s = len(s) - level  # s的真实长度
            if '.' in s:  # s是一个文件
                res = max(res, prefix[level] + len_s)  # 比较长度
            elif level + 1 < len(prefix):  # s是文件夹，将当前层的字符串长度保存
                prefix[level + 1] = prefix[level] + len_s + 1
            else:  # +1是要加上分隔符/
                prefix.append(prefix[-1] + len_s + 1)
        return res
