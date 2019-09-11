'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array or len(array) == 1:
            return array
        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 == 0:
                even.append(array[i])
            else:
                odd.append(array[i])
        return odd + even

        # solution 2
        if not array or len(array) == 1:
            return array
        l = 0
        r = len(array)
        while l < r:
            if array[l] % 2 == 0:
                array.append(array.pop(l))
                r -= 1
            else:
                l += 1
        return array