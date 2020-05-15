from randomList import randomList
from typing import List

iList = randomList.randomList(20)


def insertSort(iList: List) -> List:
    if len(iList) <= 1:
        return iList
    for right in range(1, len(iList)):  # 遍历
        target = iList[right]  # 右侧数据的第一个值
        for left in range(0, right):  # 遍历左侧所有的值
            if target < iList[left]:  # 如果右侧的数据小于左侧的
                iList[left+1:right+1] = iList[left:right]  # 左侧数据下一位开始整体后移
                iList[left] = target
                break
        print("第{}轮排序结果".format(right), end="")
        print(iList)

    return iList


if __name__ == '__main__':
    print("原始数据", iList)
    print(insertSort(iList))