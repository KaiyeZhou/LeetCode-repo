# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ## 快慢指针
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        ###
        # num = 1
        # tmp = head
        # while tmp.next != None:
        #     tmp = tmp.next
        #     num += 1
        # idx = num - n
        # if idx == 0:
        #     # re_head = head.next
        #     #del head
        #     return head.next
        # else:
        #     num = 1
        #     tmp = head
        #     while num != idx:
        #         tmp = tmp.next
        #         num += 1
        #     # del_node = tmp.next
        #     tmp.next = tmp.next.next
        #     #del del_node
        #     return head