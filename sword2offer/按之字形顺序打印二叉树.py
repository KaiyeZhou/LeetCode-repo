'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack1 = [pRoot]
        stack2 = []
        result = []
        while stack1 or stack2:
            ret1 = []            # 暂存各层的节点值
            ret2 = []            # 暂存各层的节点值
            while stack1:
                node = stack1.pop()
                # 按从左到右入栈2
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                ret1.append(node.val)
            if len(ret1) != 0:
                result.append(ret1)
            while stack2:
                node = stack2.pop()
                # 按从右到左入栈1
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
                ret2.append(node.val)
            if len(ret2) != 0 :
                result.append(ret2)
        return result

        # 第二种方法，判断奇数层和偶数层
        if pRoot == None:
            return []
        rootlist = [pRoot]
        res = []
        n = 1
        while rootlist:
            templist = []
            tempres = []
            # for node in rootlist:
            #     tempres.append(node.val)
            #     if node.left:
            #         templist.append(node.left)
            #     if node.right:
            #         templist.append(node.right)
            while rootlist:
                node = rootlist.pop(0)
                tempres.append(node.val)
                if node.left:
                    templist.append(node.left)
                if node.right:
                    templist.append(node.right)
            if n % 2 == 0:
                tempres.reverse()
            res.append(tempres)
            n += 1
            rootlist = templist
        return res