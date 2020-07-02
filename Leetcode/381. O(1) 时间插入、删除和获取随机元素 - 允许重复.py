# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/2 17:54
 @Author  : QDY
 @FileName: 381. O(1) 时间插入、删除和获取随机元素 - 允许重复.py

    设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
    注意: 允许出现重复元素。

    insert(val)：向集合中插入元素 val。
    remove(val)：当 val 存在时，从集合中移除一个 val。
    getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。

    示例:

    // 初始化一个空的集合。
    RandomizedCollection collection = new RandomizedCollection();

    // 向集合中插入 1 。返回 true 表示集合不包含 1 。
    collection.insert(1);

    // 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
    collection.insert(1);

    // 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
    collection.insert(2);

    // getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
    collection.getRandom();

    // 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
    collection.remove(1);

    // getRandom 应有相同概率返回 1 和 2 。
    collection.getRandom();

"""
import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        HashSet + List
        """
        self.Dict = defaultdict(set)
        self.List = []
        self.Len = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection.
        Returns true if the collection did not already contain the specified element.
        """

        self.List.append(val)
        self.Dict[val].add(self.Len)
        self.Len += 1
        return len(self.Dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # print(self.List,self.Dict,self.Len,val)
        if val not in self.Dict:
            return False
        else:
            val_id = self.Dict[val].pop()  # 待删除值在List中的位置
            if not self.Dict[val]:
                del self.Dict[val]
            if val_id == self.Len - 1:
                self.List.pop()
            else:
                self.List[val_id] = self.List.pop()  # 将List最后一个元素x放到List[val_id]上
                self.Dict[self.List[val_id]].discard(self.Len - 1)  # 从Dict[x]中把索引为Len-1的去掉
                self.Dict[self.List[val_id]].add(val_id)  # Dict[x]中添加上新的索引val_id
            self.Len -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.List)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
