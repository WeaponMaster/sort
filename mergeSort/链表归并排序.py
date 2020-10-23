from typing import Optional

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


def sortList(head: ListNode) -> Optional[ListNode]:
    # 递归终止条件
    if head is None:
        return None

    if head.next is None:
        return head

    # 双指针寻找链表中点
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 中点处切断链表，得到两个链表
    mid = slow.next  # 切分链表后下半部分链表的头部
    slow.next = None

    # 递归
    l1 = sortList(head)
    l2 = sortList(mid)
    return merge(l1, l2)


# 合并函数
def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
        # l1链表已经取完
        if l1 is None:
            cur.next = l2
            break
        # l2链表已经取完
        if l2 is None:
            cur.next = l1
            break

        if l1.data >= l2.data:
            cur.next = ListNode(l2.data)
            cur = cur.next
            l2 = l2.next
        else:
            cur.next = ListNode(l1.data)
            cur = cur.next
            l1 = l1.next
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
    print(listres(sortList(node1)))
