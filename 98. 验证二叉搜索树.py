# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 中序遍历，得到数组是升序
#         inorder = self.inorder(root)
#         return inorder == list(sorted(set(inorder)))
    
#     def inorder(self, root):
#         if not root:
#             return []
#         return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        
        # 递归法
#         self.pre = None
#         return self.helper(root)
    
#     def helper(self, root):
#         if root is None:
#             return True
#         if not self.helper(root.left):
#             return False
#         if self.pre and self.pre.val >= root.val:
#             return False
#         self.pre = root
#         return self.helper(root.right)
        
        ##
#         return self.ValidBST(root, -2**32, 2**32 - 1)
    
#     def ValidBST(self, root, min, max):
#         if root is None:
#             return True
#         if root.val <= min or root.val >= max:
#             return False
#         return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
        
        ### 
#         def inorderTraversal(root): 
#             if root == None:
#                 return []
#             res = []
#             res += inorderTraversal(root.left)
#             res.append(root.val)
#             res += inorderTraversal(root.right)
#             return res
        
#         res = inorderTraversal(root)
#         if res != sorted(list(set(res))): return False
#         return True
        
        ####
        if not root:
            return True

        pre = None
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and root.val <= pre.val:
                        return False
                
                pre = root
                root = root.right

        return True