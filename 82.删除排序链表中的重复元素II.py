# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while head and head.next:
            if head.val == head.next.val:
                head = head.next
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next     # 防止重复元素之前存在不重复的元素，不加这一步，不重复的元素就被删除了
            head = head.next
        return dummy.next

        # 遍历一遍，生成哈希表
        only_list = []   # 顺序表
        only_dict = {}   # 哈希表
        while head:
            if head.val in only_dict:
                only_dict[head.val] += 1
            else:
                only_list.append(head.val)
                only_dict[head.val] = 1
            head = head.next
        
        dummy = ListNode(-1)
        p = dummy
        for i in only_list:
            if only_dict[i] == 1:
                p.next = ListNode(i)
                p = p.next
        return dummy.next