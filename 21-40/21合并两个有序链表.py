'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
在leetcode测试环境中无需以上代码,在本地测试环境中需要
'''

class Solution:
    def mergeTwoLists(self, list1, list2):
        # 创建一个虚拟头节点
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # 如果其中一个链表还有剩余节点，直接连接到新链表末尾
        current.next = list1 if list1 else list2
        return dummy.next
# 测试
if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    merged_list = Solution().mergeTwoLists(l1, l2)
    while merged_list:
        print