# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/27 17:02
 @Author  : QDY
 @FileName: 208. 实现 Trie (前缀树).py

    实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

    示例:

    Trie trie = new Trie();

    trie.insert("apple");
    trie.search("apple");   // 返回 true
    trie.search("app");     // 返回 false
    trie.startsWith("app"); // 返回 true
    trie.insert("app");
    trie.search("app");     // 返回 true
    说明:

    你可以假设所有的输入都是由小写字母 a-z 构成的。
    保证所有输入均为非空字符串。

"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {'is_word': False}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {'is_word': False}
            cur = cur[char]
        cur['is_word'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        if cur['is_word']:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
