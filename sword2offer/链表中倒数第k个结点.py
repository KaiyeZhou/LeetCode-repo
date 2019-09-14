'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        fast = slow = head
        for _ in range(k - 1):
            fast = fast.next
        if not fast:
            return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow