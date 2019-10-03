'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        res = [1]
        id2, id3, id5 = 0, 0, 0
        for i in range(1, index):
            res.append(min(res[id2] * 2, res[id3] * 3, res[id5] * 5))
            if res[i] == res[id2] * 2:
                id2 += 1
            if res[i] == res[id3] * 3:
                id3 += 1
            if res[i] == res[id5] * 5:
                id5 += 1
        return res[index - 1]