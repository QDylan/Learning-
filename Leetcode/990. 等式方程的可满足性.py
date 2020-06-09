class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]  # 记录每个节点的父节点，相当于指向父节点的指针
        self.size = [1] * N  # 记录着每棵树的重量,目的是让 union 后树依然拥有平衡性
        self.count = N  # 记录连通分量个数

    def union(self, p, q):  # 将p,q连通
        root_p = self.find(p)  # 查询p,q的父节点
        root_q = self.find(q)  # 将父节点相连
        if root_p == root_q:  # p,q已经是连通的
            return

        if self.size[root_p] > self.size[root_q]:  # 将较小的树接到较大的树下(平衡性优化)
            self.parent[root_q] = root_p  # 更新root_q的父节点为root_p
            self.size[root_p] += self.size[root_q]  # 更新root_p的重量
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]

        self.count -= 1

    def find(self, p):  # 查询p的父节点
        while self.parent[p] != p:  #
            self.parent[p] = self.parent[self.parent[p]]  # 顺便压缩路径
            p = self.parent[p]  # 保证了最终所有树高都不会超过 3
        return p

    def connected(self, p, q):  # 查询p和q是否连通
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q


class Solution:
    def equationsPossible(self, equations):
        uf = UF(26)  # 26个字母
        for eq in equations:
            if eq[1] == '=':  # ord('a')=97
                uf.union(ord(eq[0]) - 97, ord(eq[3]) - 97)
        for eq in equations:
            if eq[1] == '!':
                if uf.connected(ord(eq[0]) - 97, ord(eq[3]) - 97):
                    return False
        return True

        # equal = []
        # not_equal = []
        # for item in equations:
        #     if '==' in item:  # 把等式的两元素以集合形式存入 equal
        #         tmp = item.split('==')
        #         new = True
        #         if equal:  #
        #             prev = -1
        #             i = 0
        #             while i < len(equal) :  # 在equal中查找是否已有相同的元素出现
        #                 if tmp[0] in equal[i] or tmp[1] in equal[i]:
        #                     equal[i].add(tmp[0])  # 若有，则把等式的两元素加入到已存在的集合中去
        #                     equal[i].add(tmp[1])
        #                     new = False
        #                     if prev < 0:
        #                         prev = i
        #                     else:  # 合并有相同元素的集合，保留较早出现的那个
        #                         equal[prev] = equal[prev].union(equal[i])
        #                         equal.pop(i)
        #                         continue
        #                 i += 1
        #         if new:
        #             equal.append({tmp[0],tmp[1]})
        #     else:  # 把不等式的两端元素成对的以列表形式存入not_equal中
        #         tmp = item.split('!=')
        #         if tmp[0]==tmp[-1]:return False  # 若两端元素相同则返回False
        #         not_equal.append(tmp)

        # for item in not_equal:  # 遍历not_equal中的每组不相等的两元素
        #     for item_ in equal:  # 若该两元素同时出现在equal中的某一组中，则返回False
        #         if item[0] in item_ and item[1] in item_:
        #             return False
        # return True
