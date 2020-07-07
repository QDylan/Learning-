# -*- coding: utf-8 -*-
"""
 @Time    : 2020-03-19 16:15
 @Author  : QDY
 @FileName: Sort_Methods.py
 @Software: PyCharm

 冒泡排序，鸡尾酒（双向冒泡）排序，选择排序，插入排序，希尔排序
 快速排序，桶排序，计数排序，基数排序

"""

import random, time


def bubble_sort(alist):
    # 冒泡排序，稳定，空间O(1)
    # 时间：平均O(n^2)，最好O(n)，最坏O(n^2)
    length = len(alist)
    swapped, j = True, 0
    while swapped:
        swapped = False
        for i in range(length - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True
        j += 1
    return alist
    # for i in range(length):
    #     for j in range(i + 1, length):
    #         if alist[i] > alist[j]:
    #             alist[i], alist[j] = alist[j], alist[i]
    #             # print(alist)
    # return alist


def bi_bubble_sort(alist):
    length = len(alist)
    if length < 2:
        return alist
    swapped, j = True, 0
    while swapped:
        swapped = False
        for i in range(j, length - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(length - 2 - j, -1 + j, -1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True
        j += 1
        # print(alist)
    return alist


def select_sort(alist):
    # 选择排序，不稳定，空间O(1)
    # 时间：平均O(n^2)，最好O(n^2)，最坏O(n^2)
    length = len(alist)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
        # print(alist)
    return alist


def insert_sort(alist):  #
    # 插入排序，稳定，空间O(1)
    # 时间：平均O(n^2)，最好O(n)，最坏O(n^2)
    length = len(alist)
    if length < 2:
        return alist

    for i in range(1, length):
        while i > 0:
            if alist[i] < alist[i - 1]:  # alist[i]比其前一个元素小时
                #
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
                # print(alist)
            else:
                break
    return alist


def shell_sort(alist):  # 分组的插入排序
    """
    希尔排序，不稳定，空间O(1)
    时间：最好O(n^1.25)，最坏O(n^2)
    """
    length = len(alist)
    gap = length // 2
    while gap:
        for j in range(gap):  # 分成gap组，每组做插入排序
            i = j
            while i + gap < length:
                i += gap  # i, i+gap, i+2*gap ……
                while i > j and alist[i - gap] > alist[i]:  # 插入排序
                    alist[i - gap], alist[i] = alist[i], alist[i - gap]
                    i -= gap

        gap //= 2

        print(alist)

    return alist


def quick_sort(alist):
    """
    快速排序，不稳定，空间O(logn)
    时间：最好O(nlogn)，平均O(nlogn)，最坏O(n^2)
    """
    length = len(alist)
    if length <= 1:
        # print(alist)
        return alist
    low = 0
    high = length - 1
    mid_value = alist[0]
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1  # high 左移指导与low相等或 high指向的值大于mid
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    alist[low + 1:] = quick_sort(alist[low + 1:])
    alist[:low] = quick_sort(alist[:low])
    # print(alist, low)
    return alist


def quick_sort_v2(alist, first=0, last=None):
    """ 快速排序 不使用切片 节省空间"""
    if last is None:
        last = len(alist) - 1
    if first >= last:
        return alist
    low, high = first, last
    mid_value = alist[first]
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    quick_sort_v2(alist, first, low - 1)
    quick_sort_v2(alist, low + 1, last)
    return alist


def quick_sort_v3(alist, first=0, last=None):
    if last is None:
        last = len(alist) - 1
    if first >= last:
        return alist
    index = random.randint(first, last)
    # 取随机值避免最坏情况
    mid_value = alist[index]
    alist[first], alist[index] = alist[index], alist[first]
    low, high = first, last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    quick_sort_v2(alist, first, low - 1)
    quick_sort_v2(alist, low + 1, last)
    return alist


def bucket_sort(alist):
    """
    桶排序，稳定，空间不定
    时间：O(n)
    缺点：
        1.待排序的元素不能是负数,小数.
        2.空间复杂度不确定,要看待排序元素中最大值是多少.
        所需要的辅助数组大小即为最大元素的值.
    """
    max_value = max(alist) + 1
    bucket = [0] * max_value
    for i in alist:
        bucket[i] += 1

    pos = 0
    for i in range(max_value):
        while bucket[i] != 0:
            alist[pos] = i
            pos += 1
            bucket[i] -= 1

    return alist


def merge_sort(alist):
    """
    归并排序，稳定，空间O(n)
    时间：O(nlogn)
    """
    length = len(alist)
    if length <= 1:
        return alist
    mid = length // 2
    left_list = merge_sort(alist[:mid])  # 拆分
    right_list = merge_sort(alist[mid:])

    left_cur, right_cur = 0, 0
    pos = 0
    while left_cur < len(left_list) and right_cur < len(right_list):  # 合并两个有序数组
        if left_list[left_cur] <= right_list[right_cur]:
            alist[pos] = left_list[left_cur]
            pos += 1
            left_cur += 1
        else:
            alist[pos] = right_list[right_cur]
            pos += 1
            right_cur += 1

    for i in left_list[left_cur:]:
        alist[pos] = i
        pos += 1
    for i in right_list[right_cur:]:
        alist[pos] = i
        pos += 1

    return alist


def radix_sort(nums):
    """
    基数排序，稳定，空间不定
    时间：O(n)
    缺点：
        1.待排序的元素不能是负数,小数.
        2.空间复杂度不确定,要看待排序元素中最大值是多少.
        所需要的辅助数组大小即为最大元素的值.
    """
    max_val = max(nums)
    max_r = len(str(max_val))
    bucket = [[] for i in range(10)]
    bucket_ = [[] for i in range(10)]

    for i in nums:  # 按个位数放入
        bucket[i % 10].append(i)
    r = 2
    while r <= max_r:
        for b in bucket:
            for item in b:  # 按r为放入
                bucket_[item % (10 ** r) // (10 ** (r - 1))].append(item)
        bucket, bucket_ = bucket_, [[] for i in range(10)]
        r += 1
    pos = 0
    for b in bucket:
        for item in b:  # 取出
            nums[pos] = item
            pos += 1
    return nums


def heap_sort(alist):
    """堆排序"""

    def heapify(arr, n, i):
        if i > n:
            return
        largest = i
        # 对于堆中id为i的节点，(由于堆是一颗完全二叉树)
        # 其父节点parent = (i-1)//2
        # 左节点 = 2*i+1，右节点 = 2*i+2
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:  # 若i的左子节点存在且大于i节点的值
            largest = left
        if right < n and arr[largest] < arr[right]:  # 若i的右子节点存在且大于i节点的值
            largest = right
        # largest 为 比根节点大的 子节点
        if largest != i:  # 若i有变化，则交换元素
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)  # 此时largest位置的值为arr[i]，继续对该节点及其子树heapify

    length = len(alist)
    # 从最后一个节点到第一个节点做heapify, 构造大顶堆
    for i in range(length - 1, -1, -1):
        heapify(alist, length, i)
    # 从最后一个节点开始，一个个交换元素
    for i in range(length - 1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heapify(alist, i, 0)  # 对0~i维护

    return alist


def test_time(alist, method):
    tmp = alist.copy()
    start = time.time()
    if method == 'quick':
        quick_sort_v2(tmp)
    elif method == '快速':
        quick_sort_v3(tmp)
    print(tmp)
    print(time.time() - start)


if __name__ == '__main__':
    test = [random.randint(0, 100) for i in range(50)]
    # bubble_sort(test)
    # bi_bubble_sort(test)
    # select_sort(test)
    # insert_sort(test)
    # shell_sort(test)
    # quick_sort(test)
    # tmp = test.copy()
    # start = time.time()
    # quick_sort_v2(tmp)
    # print(tmp)
    # print(time.time() - start)
    #
    # tmp = test.copy()
    # start = time.time()
    # quick_sort_v3(tmp)
    # print(tmp)
    # print(time.time() - start)
    #
    # tmp = test.copy()
    # start = time.time()
    # merge_sort(tmp)
    # print(tmp)
    # print(time.time() - start)

    # bucket_sort(test)
    # merge_sort(test)
    # test = radix_sort(test)
    heap_sort(test)
    print(test)
