'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

https://blog.csdn.net/wang969696/article/details/95930676
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < sequence[-1]:
                return False
        left = right = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right