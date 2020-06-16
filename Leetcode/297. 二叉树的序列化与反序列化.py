# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 10:39
 @Author  : QDY
 @FileName: 297. 二叉树的序列化与反序列化.py

    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
    同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你
    只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

    示例: 
    你可以将以下二叉树：

        1
       / \
      2   3
         / \
        4   5

    序列化为 "[1,2,3,null,null,4,5]"
    提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
    你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

    说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        data = []
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node:
                    data.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    data.append(None)
        while data[-1] is None: data.pop()
        return str(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return
        i, j = 1, 1
        while data[i].isdigit() or data[i] == '-':
            i += 1
        root = TreeNode(int(data[j:i]))
        queue = [[root, 0]]
        while i < len(data):
            if data[i].isdigit() or data[i] == '-':
                j = i
                while i < len(data) and data[i].isdigit() or data[i] == '-':
                    i += 1
                new = TreeNode(int(data[j:i]))
                if not queue[0][1]:
                    queue[0][0].left = new
                    queue[0][1] += 1
                    queue.append([new, 0])
                else:
                    node, t = queue.pop(0)
                    node.right = new
                    queue.append([new, 0])
            elif data[i] == 'N':
                if not queue[0][1]:
                    queue[0][1] += 1
                else:
                    queue.pop(0)
                i += 4
            else:
                i += 1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
