# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None or m >= n:
            return head
        firstNode = ListNode(0)
        firstNode.next = head
        premNode = firstNode
        for i in range(m - 1):
            premNode = premNode.next
        
        for i in range(n - m):
            prenNode = firstNode
            for j in range(n - 1):
                prenNode = prenNode.next
            # 找到第n个节点
            nNode = prenNode.next
            prenNode.next = prenNode.next.next
            nNode.next = premNode.next
            premNode.next = nNode
            premNode = premNode.next
        return firstNode.next
        
        # 压入列表，反转后创建新的链表
        # if head ==None:
        #     return 
        # if m ==n:
        #     return head        
        # stack = []
        # first = ListNode(0)
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # stack[m-1:n] = reversed(stack[m-1:n])
        # res = first
        # while stack:
        #     first.next = ListNode(stack.pop(0))
        #     first = first.next
        # return res.next

            