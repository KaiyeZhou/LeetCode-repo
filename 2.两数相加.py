'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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
            # 为了防止l1和l2都为空，但是最后一位有进位，因此在最前面加上一个1，比如[5],[5]，输出是[0,1]
            if flag:                         # 如果flag不为0，就是对应位置相加后有进位
                res.next = ListNode(1)     # res的下一节点设为1
        res = tmp.next     ### 去掉第一个节点0
        del tmp
        return res