# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/20 11:12
 @Author  : QDY
 @FileName: 95. 不同的二叉搜索树 II.py

    给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。     

    示例：
    输入：3
    输出：
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释：
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
     
    提示：
    0 <= n <= 8

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n == 0: return []

        def build_trees(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end + 1):  # 选择一个作为根节点

                left = build_trees(start, i - 1)  # 小于i的构成左子树
                right = build_trees(i + 1, end)  # 大于i的构成又子树
                # print(start,end,i,left,right)
                for l in left:
                    for r in right:
                        new = TreeNode(i)
                        new.left = l
                        new.right = r
                        all_trees.append(new)
            return all_trees

        return build_trees(1, n)
