'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。=

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # res_min = ListNode(0)
        # res_max = ListNode(0)
        # head1 = res_min      
        # head2 = res_max
        # # tmp = head
        # while head:
        #     if head.val < x:
        #         res_min.next = head
        #         head = head.next
        #         res_min = res_min.next
        #         res_min.next = None
        #     else:
        #         res_max.next = head
        #         head = head.next
        #         res_max = res_max.next
        #         res_max.next = None
        #     # tmp = tmp.next
        # res_min.next = head2.next
        # return head1.next
        
        res_min = ListNode(0)
        res_max = ListNode(0)
        head1 = res_min
        head2 = res_max
        while head:
            if head.val < x:
                res_min.next = head
                res_min = res_min.next
            else:
                res_max.next = head
                res_max = res_max.next
            head = head.next
        res_min.next = head2.next
        res_max.next = None    #很重要，别漏了，不然超时！！！
        return head1.next

