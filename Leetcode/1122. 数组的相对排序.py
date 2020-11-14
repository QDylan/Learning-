# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-14 10:39
 @Author  : QDY
 @FileName: 1122. 数组的相对排序.py
 @Software: PyCharm
"""
"""
给你两个数组，arr1 和arr2，

arr2中的元素各不相同
arr2 中的每个元素都出现在arr1中
对 arr1中的元素进行排序，使 arr1 中项的相对顺序和arr2中的相对顺序相同。未在arr2中出现过的元素需要按照升序放在arr1的末尾。


示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2中的元素arr2[i]各不相同
arr2 中的每个元素arr2[i]都出现在arr1中

"""
class Solution:
    def relativeSortArray(self, arr1, arr2):
        N = len(arr2)
        index = [N]*(max(arr1)+1)
        for i in range(N):
            index[arr2[i]] = i
        return sorted(arr1,key=lambda x:(index[x],x))
