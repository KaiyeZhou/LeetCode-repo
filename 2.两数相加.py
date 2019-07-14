# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 如果有一个链表为空，返回另外一个链表
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # tmp是暂存（temporal）
        tmp = ListNode(0)   # 引用ListNode类定义了一个链表节点并赋给tmp
        res = tmp
        flag = 0
        while l1 or l2:
            tmp_sum = 0   # 链表节点值的和
            if l1:
                tmp_sum = l1.val
                l1 = l1.next
            if l2:         # 如果l2不为空，把l2中和l1对应的节点的值加到tmp_sum
                tmp_sum += l2.val
                l2 = l2.next
            tmp_res = (tmp_sum + flag) % 10     # 个位数字
            flag = (tmp_sum + flag) // 10      # 进位的数
            res.next = ListNode(tmp_res)
            res = res.next
            if flag:                         # 如果flag不为0，就是对应位置相加后有进位
                res.next = ListNode(1)     # res的下一节点设为1
        res = tmp.next     ### 去掉第一个节点0
        del tmp
        return res