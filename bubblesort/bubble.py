from randomList import randomList
from typing import List




def bubblesort(l: List[int]):
    """冒泡排序,从小到大"""
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):  # 外层循环控制轮数
        for j in range(len(l) - i):  # 内层循环负责交换数据
            if l[j] >= l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        print("第{}轮排序结果".format(i), end="")
        print(l)
    return l

if __name__ == '__main__':
    iList = randomList.randomList(20)
    print("原始数据", iList)
    print(bubblesort(iList))
