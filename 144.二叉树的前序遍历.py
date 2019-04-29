# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ### 递归
        # if root == None:
        #     return []
        # res = []
        # res.append(root.val)
        # res += self.preorderTraversal(root.left)
        # res += self.preorderTraversal(root.right)
        # return res
        
        ### 迭代
        if root == None:
            return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res