# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针:令fast指针先移动k步，步长为1，从而与slow指针形成k步长的窗口。然后两个指针同时移动，当fast指针到达最末尾的时候，
        # 窗口的大小就是要将其旋转到开头的大小。将fast指向head，slow指向None，则完成旋转。 k % count
        if head is None or head.next is None:
            return head
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        k = k % count
        if k == 0:
            return head
        fast = slow = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        newhead = slow.next
        fast.next = head
        slow.next = None
        return newhead

        # 第二种方法：将链表节点对应的值存到list中，通过list的insert和pop操作，每次把最后一个数添加到第一位，最后生成一个新的链表

        # 第三种方法：将原链表首尾节点相连，转化为循环链表
        if head is None or head.next is None:
            return head
        count = 1
        p = head
        while p.next:
            count += 1
            p = p.next
        p.next = head
        step = count - k % count
        while step > 0:
            p = p.next
            step -= 1
        newhead = p.next
        p.next = None
        return newhead