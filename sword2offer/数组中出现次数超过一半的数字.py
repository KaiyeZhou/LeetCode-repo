'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        dic = {}
        for item in numbers:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        nums = set(numbers)
        for item in nums:
            if dic[item] > len(numbers) // 2:
                return item
        return 0

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = numbers[0]
        count = 0
        for i in range(len(numbers)):
            if count == 0:
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1
            elif numbers[i] != res:
                count -= 1
        ct = 0
        for item in numbers:
            if item == res:
                ct += 1
        if ct > len(numbers) // 2:
            return res
        return 0