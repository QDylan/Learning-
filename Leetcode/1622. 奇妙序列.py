# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-19 10:52
 @Author  : QDY
 @FileName: 1622. 奇妙序列.py
 @Software: PyCharm
"""
"""
请你实现三个 API append，addAll和multAll来实现奇妙序列。

请实现Fancy类 ：

Fancy()初始化一个空序列对象。
void append(val) 将整数val添加在序列末尾。
void addAll(inc)将所有序列中的现有数值都增加inc。
void multAll(m)将序列中的所有现有数值都乘以整数m。
int getIndex(idx) 得到下标为idx处的数值（下标从 0 开始），并将结果对109 + 7取余。如果下标大于等于序列的长度，请返回-1。


示例：

输入：
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
输出：
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

解释：
Fancy fancy = new Fancy();
fancy.append(2);   // 奇妙序列：[2]
fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
fancy.append(7);   // 奇妙序列：[5, 7]
fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // 返回 10
fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10);  // 奇妙序列：[13, 17, 10]
fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // 返回 26
fancy.getIndex(1); // 返回 34
fancy.getIndex(2); // 返回 20

提示：

1 <= val, inc, m <= 100
0 <= idx <= 105
总共最多会有105次对append，addAll，multAll和getIndex的调用。

"""


class Fancy:

    def __init__(self):
        self.mod = 10 ** 9 + 7
        self.v = []
        self.a = 1  # 因数
        self.b = 0  # 加数

    # 快速幂
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    # 乘法逆元
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.v.append((val - self.b) * self.inv(self.a) % self.mod)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.mod
        self.b = self.b * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1
        return (self.a * self.v[idx] + self.b) % self.mod

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
