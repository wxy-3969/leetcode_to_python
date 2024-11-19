'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''


# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # 创建一个虚拟头节点，方便处理删除头节点的情况
        dummy = ListNode(0)
        dummy.next = head
        # 快指针先移动n步
        fast = dummy
        for _ in range(n):
            fast = fast.next
        # 慢指针指向虚拟头节点
        slow = dummy
        # 快慢指针同时移动，直到快指针到达链表末尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 删除倒数第n个节点
        slow.next = slow.next.next
        return dummy.next
# 测试
if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(6)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 2)
    while new_head:
        print(new_head.val)
        new_head = new_head.next