'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        res = []
        while stack:
            templist = []
            tempres = []
            while stack:
                node = stack.pop(0)
                tempres.append(node.val)
                if node.left:
                    templist.append(node.left)
                if node.right:
                    templist.append(node.right)
            # 另一种写法
            # for node in stack:
            #     tempres.append(node.val)
            #     if node.left:
            #         templist.append(node.left)
            #     if node.right:
            #         templist.append(node.right)
            res.append(tempres)
            stack = templist
        return res

        # 递归解法
    def Print(self, pRoot):
        res = []
        self.level(pRoot, 0, res)
        return res

    def level(self, root, level, res):
        if not root: return
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)
