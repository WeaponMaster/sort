"""把最小的数从前到后一次排列"""
from typing import List
from randomList import *
# from randomList import randomList



def selectionSort(iList: List[int]) -> List:
    if len(iList) <= 1:
        return iList
    for i in range(len(iList)-1):  # 外层循环控制第几轮
        minindex = i    # 指定当前轮排头的元素位置
        for j in range(i+1, len(iList)):    # 内层循环负责找到最小值索引
            if iList[j] < iList[minindex]:
                minindex = j
        iList[i], iList[minindex] = iList[minindex],iList[i]    # 交换最小值和排头数据
        print("第{}轮排序结果".format(i), end="")
        print(iList)
    return iList


if __name__ == '__main__':

    iList = randomList.randomList(20)
    print("原始数据", iList)
    print(selectionSort(iList))
    # os.path







