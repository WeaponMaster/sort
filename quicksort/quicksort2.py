"""单指针遍历法"""

from randomList import randomList


def quickSort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quickSort(array, l, q - 1)
        quickSort(array, q + 1, r)


def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


if __name__ == '__main__':
    iList = randomList.randomList(20)
    print("原列表为：%s" % iList)
    quickSort(iList, 0, len(iList) - 1)
    print("新列表为：%s" % iList)