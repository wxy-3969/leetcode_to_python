class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(self, l1, l2):
    dummy_head = NodeList()
    current = dummy_head    # 初始化一个哑节点，用于返回结果链表的头部
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        # 先计算总和，包括进位
        total = val1 + val2 + carry
        carry = total // 10
        # 创建新节点并更新当前节点的值
        current.next = NodeList(total % 10)
        current = current.next
        # 移动l1和l2指针到下一个节点（如果存在）
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy_head.next