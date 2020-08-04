# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/4 9:39
 @Author  : QDY
 @FileName: 80. 删除排序数组中的重复项 II.py
 @Software: PyCharm
"""
"""
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:
    给定 nums = [1,1,1,2,2,3],
    函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
    你不需要考虑数组中超出新长度后面的元素。
    示例 2:

    给定 nums = [0,0,1,1,1,1,2,3,3],

    函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
    你不需要考虑数组中超出新长度后面的元素。

    说明:
    为什么返回数值是整数，但输出的答案是数组呢?
    请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
    你可以想象内部操作如下:

    // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);
    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n<=2:return n
        index = 2  # 表示删除重复元素后的序列长度，也是新元素进入判断的索引
        for i in range(2,n):
            # 若nums[i]==nums[index-2]，则nums[index-2:i+1]都是相同的元素，且超过三个
            if nums[i] != nums[index-2]:  # 寻找nums[i]直到与num[index-2:index]的不相同
                nums[index] = nums[i]  # 令nums[index]=nums[i]，这样最多只有连续两个相同
                index += 1

        return index