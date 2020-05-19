"""
Author:  Mr.Zhang
Create:  2020/5/19 0:01
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""
from typing import List
from randomList import randomList

iList = randomList.randomList(20)


# 填坑法
def partition(array, start, end):
    left = start
    right = end
    pivot = array[left]
    while left < right:
        # 先从 right 游标开始移动 找到第一个比基准元素小的位置停止
        while left < right and array[right] > pivot:
            right -= 1
        array[left] = array[right]  # 循环结束后 就找到了右侧比基准元素小的数
        while left < right and array[left] <= pivot:
            left += 1
        array[right] = array[left]
    array[left] = pivot  # 循环结束后 此时left/right(因为两者已经重合)所在位置即为 基准元素所在位置
    return left


def quickSort(iList, start, end):
    if start >= end:
        return
    mid = partition(iList, start, end)
    quickSort(iList, start, mid - 1)
    quickSort(iList, mid + 1, end)


if __name__ == '__main__':
    print("原列表为：%s" % iList)
    quickSort(iList, 0, len(iList) - 1)
    print("新列表为：%s" % iList)
