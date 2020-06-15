# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/15 13:30
 @Author  : QDY
 @FileName: 1483. 树节点的第 K 个祖先_倍增_hard.py

    给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。
    树的根节点是编号为 0 的节点。
    请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。
    如果不存在这样的祖先节点，返回 -1 。

    树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

    输入：
    ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
    [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

    输出：
    [null,1,0,-1]

    解释：
    TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
    treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
    treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
    treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
     

    提示：
    1 <= k <= n <= 5*10^4
    parent[0] == -1 表示编号为 0 的节点是根节点。
    对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
    0 <= node < n
    至多查询 5*10^4 次

"""


class TreeAncestor:

    def __init__(self, n, parent):  # Binary Lifting 倍增
        # 时间复杂度 O(NlogN) 空间复杂度 O(NlogN)
        self.dp = [[i] for i in parent]  # dp[i][j]=节点i的第2^j个祖先(或者说是距离i为2^j的祖先)，第一个祖先dp[i][0]为自身
        j = 1
        while True:  # 从第2个祖先开始
            all_neg = True
            for i in range(n):  # 设置每个节点的第2^j个祖先
                tmp = -1
                if self.dp[i][j - 1] != -1:  # 节点i的第2^j个祖先=节点i的第2^(j-1)个祖先的第2^(j-1)个祖先
                    tmp = self.dp[self.dp[i][j - 1]][j - 1]
                self.dp[i].append(tmp)
                if tmp != -1: all_neg = False
            if all_neg: break  # 当所有节点的第2^j个祖先都为-1时，构筑完成，跳出循环
            j += 1
        # print(self.dp)

    def getKthAncestor(self, node, k):
        # if k==0 or node==-1:return node
        res = node
        pos = 0
        # k = k_j*(2^j)+...+k1*2+k0*1, k_j=0或1
        # 设k = 2^i1+2^i2+...+2^in
        # node的第k个祖先=(node的第2^i1个祖先)的第(2^i2+...+2^in)个祖先
        while k and res != -1:  #
            if pos >= len(self.dp[res]):  # k超过了最大祖先数量
                return -1
            if k & 1:  # 若k的右边第pos位为1，找到节点的第2^pos个祖先
                res = self.dp[res][pos]
            k >>= 1  # 寻找k最右侧的1
            pos += 1

        return res

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
