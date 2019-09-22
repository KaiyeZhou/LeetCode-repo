'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

# https://blog.csdn.net/weixin_41679411/article/details/86484715
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minstack or node <= self.minstack[-1]:
            self.minstack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]