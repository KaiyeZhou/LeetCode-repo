'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0:
            return 0.0
        if exponent == 0:
            return 1.0
        res = 1
        if exponent > 0:
            for i in range(exponent):
                res *= base
        if exponent < 0:
            for i in range(-1 * exponent):
                res *= base
            res = 1 / res
        return res

# solution 2
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        e = abs(exponent)
        tmp = base
        res = 1
        while(e > 0):
            #如果最后一位为1，那么给res乘上这一位的结果
            if (e & 1 == 1):
                res =res * tmp
            e = e >> 1
            tmp = tmp * tmp
        return res if exponent > 0 else 1/res
