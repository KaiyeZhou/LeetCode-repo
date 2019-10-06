'''
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

解答：https://blog.csdn.net/ggdhs/article/details/90243761
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        if root.val == expectNumber and not root.left and not root.right:
            res.append([root.val])
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in left + right:
            res.append([root.val] + i)
        return res

# https://blog.csdn.net/qq_37888254/article/details/89736609
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def preorder(root, expectNumber, ans, path):
            path.append(root.val)
            expectNumber -= root.val
            if expectNumber == 0 and root.left == None and root.right == None:
                ans.append([p for p in path])
            if root.left:
                preorder(root.left, expectNumber, ans, path)
            if root.right:
                preorder(root.right, expectNumber, ans, path)
            path.pop()
        
        ans = []
        path = []
        if not root:
            return ans
        preorder(root, expectNumber, ans, path)
        return ans