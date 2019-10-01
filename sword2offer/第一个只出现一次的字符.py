'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        # 1
        dic = {}
        for item in s:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] = dic[item] + 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

        # 2
        for item in s:
            if s.count(item) == 1:
                return s.index(item)
        return -1

        # 字典是无序的，本地调试ok，但是牛客网上通不过
        # dic = {}
        # nums = []
        # for i in range(len(s)):
        #     if s[i] not in nums:
        #         nums.append(s[i])
        #         dic[s[i]] = i
        #     elif s[i] in nums and s[i] in dic:
        #         del dic[s[i]]
        # res = list(dic.values())
        # print(res)
        # if len(res) == 0:
        #     return -1
        # return res[0]

s = 'google'
S = Solution()
res = S.FirstNotRepeatingChar(s)
print(res)