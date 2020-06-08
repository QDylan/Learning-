# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/8 9:45
 @Author  : QDY
 @FileName: 990. 等式方程的可满足性.py

    给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
    并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
    只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

    示例 1：
    输入：["a==b","b!=a"]
    输出：false
    解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

    示例 2：
    输出：["b==a","a==b"]
    输入：true
    解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

    示例 3：
    输入：["a==b","b==c","a==c"]
    输出：true

    示例 4：
    输入：["a==b","b!=c","c==a"]
    输出：false

    示例 5：
    输入：["c==c","b==d","x!=z"]
    输出：true

"""
class Solution:
    def equationsPossible(self, equations):
        equal = []
        not_equal = []
        for item in equations:
            if '==' in item:  # 把等式的两元素以集合形式存入 equal
                tmp = item.split('==')
                new = True
                if equal:  #
                    prev = -1
                    i = 0
                    while i < len(equal) :  # 在equal中查找是否已有相同的元素出现
                        if tmp[0] in equal[i] or tmp[1] in equal[i]:
                            equal[i].add(tmp[0])  # 若有，则把等式的两元素加入到已存在的集合中去
                            equal[i].add(tmp[1])
                            new = False
                            if prev < 0:
                                prev = i
                            else:  # 合并有相同元素的集合，保留较早出现的那个
                                equal[prev] = equal[prev].union(equal[i])
                                equal.pop(i)
                                continue
                        i += 1
                if new:
                    equal.append({tmp[0],tmp[1]})
            else:  # 把不等式的两端元素成对的以列表形式存入not_equal中
                tmp = item.split('!=')
                if tmp[0]==tmp[-1]:return False  # 若两端元素相同则返回False
                not_equal.append(tmp)
        # print(equal,not_equal)
        for item in not_equal:  # 遍历not_equal中的每组不相等的两元素
            for item_ in equal:  # 若该两元素同时出现在equal中的某一组中，则返回False
                if item[0] in item_ and item[1] in item_:
                    return False

        return True