'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

假设从链表头节点到入环点的距离是 D，从入环点到两个指针首次相遇点的距离是 S1，从首次相遇点回到入环点的距离是 S2。

p 指针和 q 指针首次相遇时，各自走的距离为：L(q) = D+S1，L(p) = D+S1+S2+S1。
由于 p 指针的速度是 q 的 2 倍，所以所走的距离也是 q 的 2 倍，因此：2(D+S1) = D+2S1+S2，即为：D = S2。
从公式可以看出，从链表头节点到入环点的距离，等于从首次相遇点回到入环点的距离。因此我们重新选择两个速度一致的节点，一个从头节点位置出发，另一个从首次相遇点出发，那么，它们最终相遇的节点，就是入环点。
————————————————
版权声明：本文为CSDN博主「hresh」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Herishwater/article/details/96433817
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        pFast = pHead
        pSlow = pHead
        while pFast != None and pFast.next != None:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast == None or pFast.next == None:
            return None
        pFast = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast