# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root
        