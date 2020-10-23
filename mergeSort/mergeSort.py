from randomList import randomList
from typing import List

iList = randomList.randomList(20)


def mergeSort(iList: List):
    if len(iList) <= 1:
        return iList
    middle = len(iList) // 2
    left, right = iList[0:middle], iList[middle:]
    return merge1(mergeSort(left), mergeSort(right))


def merge(left: List, right: List):
    """对Python优化的归并"""
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    while left:
        mList.append(left.pop(0))
    while right:
        mList.append(right.pop(0))
    return mList


def merge1(left: List, right: List):
    """传统归并"""
    left_len = len(left)
    right_len = len(right)
    mList = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            mList.append(left[i])
            i += 1
        else:
            mList.append(right[j])
            j += 1

    mList.extend(left[i:])
    mList.extend(right[j:])
    return mList


if __name__ == '__main__':
    print("原始数据", iList)
    print(mergeSort(iList))
    # print(m)



