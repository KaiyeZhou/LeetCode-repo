'''
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# https://blog.csdn.net/qq_17550379/article/details/85157903
# https://cloud.tencent.com/developer/article/1407145

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 正确的二叉搜索树的中序遍历结果是递增的，利用这个定理，在中序遍历树的过程中寻找不满足条件的结点。               
        # 递归
        self.pre = None
        self.m1, self.m2 = None, None
        self.inorderTraversal(root)
        self.m1.val, self.m2.val = self.m2.val, self.m1.val
    
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            if self.pre != None and self.pre.val > root.val:
                if self.m1 == None:
                    self.m1 = self.pre
                self.m2 = root
            self.pre = root
            self.inorderTraversal(root.right)
        
        # 迭代
        cur, pre = root, None
        first, second = None, None
        stack = []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:        
                node = stack.pop()
                if pre and pre.val >= node.val:
                    if not first:
                        first = pre
                    second = node
                    
                pre = node
                cur = node.right
        
        first.val, second.val = second.val, first.val