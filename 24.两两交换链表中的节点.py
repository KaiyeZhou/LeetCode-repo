# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if head is None or head.next is None:
        #     return head
        # dummy = ListNode(-1)
        # dummy.next = head
        # temp = dummy
        # while temp.next and temp.next.next:
        #     node1 = temp.next
        #     node2 = temp.next.next
        #     temp.next = node2
        #     node1.next = node2.next
        #     node2.next = node1
        #     temp = temp.next.next
        # return dummy.next
        
        # 只额外添加一个node，比上述解法少添加一个node2
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node = temp.next.next
            temp.next.next = node.next
            node.next = temp.next
            temp.next = node
            temp = temp.next.next
        return dummy.next
        
        # 递归
        # if not head or not head.next:
        #     return head
        # pnext = head.next
        # head.next = self.swapPairs(pnext.next)
        # pnext.next = head
        # return pnext
