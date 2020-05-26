# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/26 22:21
 @Author  : QDY
 @FileName: 1457. 二叉树中的伪回文路径_DFS_BFS.py

    给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
    请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
     
    示例 1：
    输入：root = [2,3,1,3,1,null,1]
    输出：2
    解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
         在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。

    示例 2：
    输入：root = [2,1,1,1,3,null,null,null,null,null,1]
    输出：1
    解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
         这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。


    示例 3：
    输入：root = [9]
    输出：1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root):
        # 伪回文序列：至多只有一种元素出现了奇数次
        if not root: return 0
        res = 0

        def dfs(root, hash_map, odd):  # 深度优先遍历找出所有路径，同时记录每个元素的出现次数
            nonlocal res
            if not root.left and not root.right:  # 到达叶子节点
                # print(hash_map,odd)
                if odd <= 1:  # 检查
                    res += 1
                return
            if root.left:
                tmp = hash_map.copy()
                if root.left.val in tmp:
                    tmp[root.left.val] += 1
                    if tmp[root.left.val] % 2 == 0:
                        tmp_odd = odd - 1
                    else:
                        tmp_odd = odd + 1
                else:
                    tmp[root.left.val] = 1
                    tmp_odd = odd + 1
                dfs(root.left, tmp, tmp_odd)
            if root.right:
                tmp = hash_map.copy()
                if root.right.val in tmp:
                    tmp[root.right.val] += 1
                    if tmp[root.right.val] % 2 == 0:
                        tmp_odd = odd - 1
                    else:
                        tmp_odd = odd + 1
                else:
                    tmp[root.right.val] = 1
                    tmp_odd = odd + 1
                dfs(root.right, tmp, tmp_odd)

        dfs(root, {root.val: 1}, 1)
        return res

        # queue = [[root]]
        # tmp = []
        # while queue:  # 广度优先遍历找出所有路径
        #     length = len(queue)
        #     for i in range(length):
        #         node = queue.pop(0)
        #         if node[-1].left:
        #             queue.append(node+[node[-1].left])
        #         if node[-1].right:
        #             queue.append(node+[node[-1].right])
        #         if not node[-1].left and not node[-1].right:  # 叶子
        #             tmp.append([n.val for n in node])
        # res = 0
        # for list_ in tmp:  # 判断每条路径是否是伪回文序列
        #     odd = 0
        #     for item in set(list_):
        #         if list_.count(item) % 2 != 0:
        #             odd += 1
        #         if odd > 1:
        #             break
        #     if odd <= 1:
        #         res += 1
        # return res
