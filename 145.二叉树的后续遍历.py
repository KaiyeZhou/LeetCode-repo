# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## 递归
        # if root == None:
        #     return []
        # res = []
        # res += self.postorderTraversal(root.left)
        # res += self.postorderTraversal(root.right)
        # res.append(root.val)
        # return res
        
        ## 迭代
        # if root == None:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return res[::-1]
        
        ##
#         result = list()
#         if root == None:
#             return result
        
#         stack = list()
#         stack.append(root)
#         while len(stack) != 0:
#             top = stack.pop()
#             if top.left != None:
#                 stack.append(top.left)
#             if top.right != None:
#                 stack.append(top.right)

#             result.insert(0, top.val)
                
#         return result
        
        ## 参考中序遍历的思路
        result = list()
        if root == None:
            return result
        
        stack = list()
        while stack or root:
            if root:
                stack.append(root)
                result.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return result
