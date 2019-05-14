class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 0:
        #     return 0
        # tmp = res = ""
        # for item in s:
        #     if item not in tmp:
        #         tmp += item
        #         if len(tmp) > len(res):
        #             res = tmp
        #     else:
        #         i = tmp.index(item)
        #         if i == len(tmp) - 1:             #如果到达末尾
        #             tmp = item
        #         else:
        #             tmp = tmp[i + 1:] + item
        #         if len(tmp) > len(res):
        #             res = tmp
        # return len(res)
        
        ### 2
        if len(s) == 0:
            return 0
        d = {}                                       # 定义一个字典，存储不重复的字符和字符所在的下标
        start = 0                                    # 记录最近重复字符所在的位置
        length = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:       # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            length = max(length, tmp)
        return length