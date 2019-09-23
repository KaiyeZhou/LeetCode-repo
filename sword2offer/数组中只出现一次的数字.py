'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic = dict()
        for item in array:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        res = []
        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res

# solution 2
'''
用异或求解。异或运算的性质：任何一个数字异或它自己都等于0 。如果数组中只有一个数字出现过一次，其余数字都出现了两次；
这样的话如果我们从头到尾依次异或数组中的每一个数字，那么最终的结果刚好是那个只出现一次的数字，因为那些出现两次的数字全部在异或中抵消掉了。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor = 0
        for item in array:
            xor ^= item
        res1, res2 = 0, 0
        idx = 1
        while xor & idx == 0:
            idx <<= 1
        for item in array:
            if item & idx == 0:
                res1 ^= item
            else:
                res2 ^= item
        return [res1, res2]