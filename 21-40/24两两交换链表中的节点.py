'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
'''



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
'''
以上代码在本地测试时需要,在leetcode上不需要
'''


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # 新的头节点是原来的第二个节点
        new_head = head.next
        prev = None
        current = head
        while current and current.next:
            next_node = current.next
            next_next_node = next_node.next
            # 将当前节点的下一个节点指向交换后的下一个节点（即原来的下下个节点）
            current.next = next_next_node
            # 将下一个节点（即将要交换到前面的节点）的下一个节点指向当前节点
            next_node.next = current
            if prev:
                prev.next = next_node
            prev = current
            current = next_next_node
        return new_head
# 测试
if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4    
    result = solution.swapPairs(node1)
    while result:
        print(result.val, end=" ")
        result = result.next
    
