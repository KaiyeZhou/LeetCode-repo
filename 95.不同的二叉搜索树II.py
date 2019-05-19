# https://blog.csdn.net/yangjingjing9/article/details/77069723

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        else:
            return self.genBST(1, n)
    
    def genBST(self, start, end):
        res = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            lefts = self.genBST(start, i - 1)
            rights = self.genBST(i + 1, end)
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res