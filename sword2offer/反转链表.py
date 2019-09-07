'''
输入一个链表，反转链表后，输出新链表的表头。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        list1 = []
        while pHead:
            list1.append(pHead.val)
            pHead = pHead.next
        head = ListNode(0)
        res = head
        while list1:
            head.next = ListNode(list1.pop())
            head = head.next
        return res.next

        # solution 2
        if not pHead:
            return pHead
        newhead = None
        while pHead:
            tmp = pHead.next
            pHead.next = newhead
            newhead = pHead
            pHead = tmp
        return newhead