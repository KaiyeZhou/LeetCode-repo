'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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

        # solution 3
        if head == None or head.next == None or m >= n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for i in range(m - 1):
            start = start.next
        end = cur = start.next
        pre = None
        for i in range(n - m + 1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        start.next = pre
        end.next = cur
        return dummy.next