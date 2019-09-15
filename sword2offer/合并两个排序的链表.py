'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        newhead = ListNode(0)
        res = newhead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                newhead.next = pHead1
                pHead1 = pHead1.next
            else:
                newhead.next = pHead2
                pHead2 = pHead2.next
            newhead = newhead.next
        if pHead1:
            newhead.next = pHead1
        if pHead2:
            newhead.next = pHead2
        return res.next


        # 不破坏pHead1 和 pHead2
        if not pHead1 and not pHead2:
            return None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        newhead = ListNode(0)
        res = newhead
        while pHead1 or pHead2:
            if not pHead1 and pHead2:
                newhead.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
                newhead = newhead.next
            if not pHead2 and pHead1:
                newhead.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
                newhead = newhead.next
            if pHead1 and pHead2:
                if pHead1.val <= pHead2.val:
                    newhead.next = ListNode(pHead1.val)
                    pHead1 = pHead1.next
                else:
                    newhead.next = ListNode(pHead2.val)
                    pHead2 = pHead2.next
                newhead = newhead.next
        return res.next