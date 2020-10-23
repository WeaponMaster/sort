class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


def insertionSortList(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    # 创建一个新链表
    pre = dummy

    # 遍历原链表
    cur = head
    while cur is not None:  # 把待排序的结点挨个遍历一下
        temp = cur.next  # 记录下次查询的位置

        # 对已排序好的链表进行遍历,找到待插入结点的位置
        while pre.next is not None and pre.next.data < cur.data:
            pre = pre.next

        # 已确定插入位置，完成插入
        cur.next = pre.next  # 安排后事
        pre.next = cur  # 处理前面结点

        # pre、cur改变（为下一次循环做准备）
        cur = temp
        pre = dummy

    return dummy.next


def listres(head: ListNode):
    curr = head
    res = ''
    while curr:
        res = res + f'{curr} -->'
        curr = curr.next
    return res + 'END'


if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node4 = ListNode(2)
    node5 = ListNode(6)
    node6 = ListNode(1)
    node7 = ListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None
    print(listres(node1))
    print(listres(insertionSortList(node1)))
