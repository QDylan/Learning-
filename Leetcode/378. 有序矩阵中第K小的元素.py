# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 17:24
 @Author  : QDY
 @FileName: 378. 有序矩阵中第K小的元素.py

    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

    示例：
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,

    返回 13。
     
    提示：
    你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

"""


class Solution:
    def kthSmallest(self, matrix, k):
        # N个有序数组合并

        n = len(matrix)
        index = [[i, 0] for i in range(n)]  # 维护一个升序值的数组的索引列表 时间O(KlongK)

        def heapify(i):
            len_ = len(index)
            if i >= len_: return
            l, r, smallest = 2 * i + 1, 2 * i + 2, i
            if l < len_ and matrix[index[smallest][0]][index[smallest][1]] > matrix[index[l][0]][index[l][1]]:
                smallest = l
            if r < len_ and matrix[index[smallest][0]][index[smallest][1]] > matrix[index[r][0]][index[r][1]]:
                smallest = r
            if smallest != i:
                index[smallest], index[i] = index[i], index[smallest]
                heapify(smallest)

        for i in range(k - 1):

            if index[0][1] < n - 1:
                index[0][1] += 1
                heapify(0)  # 用堆的方式查找
            else:
                index[0] = index.pop()
                heapify(0)

            # cur = index.pop(0)
            # if cur[1] < n-1:
            # l,r = 0,len(index)-1
            # while l<=r:  # 二分法查找cur的位置
            #     mid = l + (r-l)//2
            #     if matrix[index[mid][0]][index[mid][1]]>matrix[cur[0]][cur[1]]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # index.insert(l,cur)
            # print(index)
        return matrix[index[0][0]][index[0][1]]

        # heap = []  # 维护一个最大长度为K的大顶堆
        # length = 0
        # n = len(matrix)
        # def heapify(i):
        #     if i >= length:return
        #     largest,l,r = i,2*i+1,2*i+2
        #     if l<length and heap[l]>heap[largest]:
        #         largest = l
        #     if r<length and heap[r]>heap[largest]:
        #         largest = r
        #     if largest!=i:
        #         heap[largest],heap[i] = heap[i],heap[largest]
        #         heapify(largest)

        # for i in range(n):
        #     for j in range(n):
        #         if length < k:
        #             heap.append(matrix[i][j])
        #             son = length
        #             pa = (son-1)//2
        #             while son>0 and heap[pa]<heap[son]:
        #                 heap[pa],heap[son] = heap[son], heap[pa]
        #                 pa, son = (pa-1)//2, pa
        #             length += 1
        #         elif length==k and matrix[i][j]<heap[0]:
        #             heap[0] = matrix[i][j]
        #             heapify(0)
        # return heap[0]
