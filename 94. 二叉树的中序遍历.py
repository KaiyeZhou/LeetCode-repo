# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## 递归
        # if root == None:
        #     return []
        # res = []
        # res += self.inorderTraversal(root.left)
        # res.append(root.val)
        # res += self.inorderTraversal(root.right)
        # return res
        
        ## 迭代
        if root == None:
            return []
        res = list()
        
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res