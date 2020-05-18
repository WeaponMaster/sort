from typing import List
from randomList import randomList

iList = randomList.randomList(20)


def quick_sort(iList, left, right):
    if left >= right:
        return
    low = left
    high = right
    pivot = iList[low]
    while left < right:
        while left < right and iList[right] > pivot:  # 先从 right 游标开始移动 找到第一个比基准元素小的位置停止
            right -= 1
        iList[left] = iList[right]  # 循环结束后 就找到了右侧比基准元素小的数
        while left < right and iList[left] <= pivot:
            left += 1
        iList[right] = iList[left]
    iList[left] = pivot  # 循环结束后 此时left/right(因为两者已经重合)所在位置即为 基准元素所在位置
    quick_sort(iList, low, left - 1)
    quick_sort(iList, left + 1, high)


if __name__ == '__main__':
    print("原列表为：%s" % iList)
    quick_sort(iList, 0, len(iList) - 1)
    print("新列表为：%s" % iList)
