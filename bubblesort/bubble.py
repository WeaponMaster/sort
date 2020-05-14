from randomList import randomList
from typing import *

iList = randomList.randomList(20)


def bubblesort(l: List[int]):
    """冒泡排序"""
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        for j in range(len(l) - i):
            if l[j] >= l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        print("第{}轮排序结果".format(i), end="")
        print(l)
    return l


if __name__ == '__main__':
    print("原始数据", iList)
    print(bubblesort(iList))
