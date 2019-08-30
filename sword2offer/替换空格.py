'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
           return s
        tmp = []
        for i in range(len(s)):
           if s[i] == ' ':
               tmp.append(i)
        ss = list(s)
        for i in range(len(tmp) - 1, -1, -1):
           ss[tmp[i]] = '%20'
        sss = ''.join(ss)
        return sss

        # solution 2
        if not s:
            return s
        ss = list(map(str, s.split(' ')))
        sss = '%20'.join(ss)
        return sss