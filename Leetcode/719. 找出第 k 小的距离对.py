# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/16 9:17
 @Author  : QDY
 @FileName: 719. 找出第 k 小的距离对.py

    给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

    示例 1:
    输入：
    nums = [1,3,1]
    k = 1
    输出：0
    解释：
    所有数对如下：
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。

    提示:
    2 <= len(nums) <= 10000.
    0 <= nums[i] < 1000000.
    1 <= k <= len(nums) * (len(nums) - 1) / 2.

"""


class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        def fesiable(distance):  # 判断距离为distance在所有数对距离的排名是否>=k
            cnt, left, = 0, 0
            for right in range(n):  # cnt 统计有多少个距离是<distacne的
                while nums[right] - nums[left] > distance:
                    left += 1  # 对于固定的右边界right，搜索最小的左边界left，使得nums[i]-nums[left]<=distance
                cnt += right - left  # 以right为右边界，有right-left个左边界满足 距离<distance
            return cnt >= k

        l, r = 0, nums[-1] - nums[0]
        while l <= r:  # 二分查找第k个距离
            m = l + (r - l) // 2
            if fesiable(m):
                r = m - 1
            else:
                l = m + 1
        return l
