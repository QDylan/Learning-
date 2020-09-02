# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-02 15:25
 @Author  : QDY
 @FileName: 173. 二叉搜索树迭代器.py
 @Software: PyCharm
"""
"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。



提示：

next()和hasNext()操作的时间复杂度是O(1)，并使用O(h) 内存，其中h是树的高度。
你可以假设next()调用总是有效的，也就是说，当调用 next()时，BST 中至少存在一个下一个最小的数。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:  # 只存左节点
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        res = node.val
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not not self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
