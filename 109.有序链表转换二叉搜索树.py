'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 将链表转换为数组，同108题
#         if not head:
#             return None
#         l = list()
#         while head:
#             l.append(head.val)
#             head = head.next 
        
#         def sortedArrayToBST(nums):
#             if not nums:
#                 return None
#             mid = len(nums) // 2
#             root = TreeNode(nums[mid])
#             root.left = sortedArrayToBST(nums[:mid])
#             root.right = sortedArrayToBST(nums[mid+1:])
#             return root
        
#         return sortedArrayToBST(l)
        
        # 快慢指针找链表中点，
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        part1 = head
        part2 = slow.next
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(part1)
        root.right = self.sortedListToBST(part2)
        return root