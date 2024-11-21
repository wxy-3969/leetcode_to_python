'''
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
'''
以上代码在本地测试时需要,在LeetCode上不需要
'''
        
class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while head:
            group_start = head
            group_end = self.get_group_end(head, k)    # 获取当前组的末尾节点   
            if not group_end:
                break
            next_group_start = group_end.next
            reversed_group_head = self.reverse_group(group_start, group_end)    # 翻转当前组内的节点    
            prev_group_end.next = reversed_group_head
            group_start.next = next_group_start
            prev_group_end = group_start
            head = next_group_start
        return dummy.next
    '''
    获取当前组的末尾节点

    '''
    
    def get_group_end(self, node, k):
        while node and k > 1:
            node = node.next
            k -= 1
        return node
    
    '''
    翻转当前组内的节点
    '''
    
    def reverse_group(self, start, end):
        prev = None
        current = start
        while current!= end:
            next_node = current.next    # 保存当前节点的下一个节点
            current.next = prev
            prev = current
            current = next_node
        end.next = prev
        return end