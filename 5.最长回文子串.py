class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## 超时
        # if not s:return ''
        # res = s[0]
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j]:
        #             if s[i:j+1] == s[i:j+1][::-1]:
        #                 # res = s[i:j+1] if (len(s[i:j+1]) >= len(res)) else res
        #                 if len(s[i:j+1]) >= len(res):
        #                        res = s[i:j+1]
        # return res

        ### 
        # mlen = len(s)
        # if mlen == 0:
        #         return ""
        # while True:
        #     i = 0
        #     while i + mlen <= len(s):
        #         sl = s[i:i + mlen]
        #         sr = sl[::-1]
        #         if sl == sr:
        #             return sl
        #         i = i + 1
        #     mlen = mlen - 1
        
        ### 动态规划
        # # 使用动态规划，用空间换时间，把问题拆分
        # # 获取字符串s的长度
        # str_length = len(s)
        # # 记录最大字符串长度
        # max_length = 0
        # # 记录位置
        # start = 0
        # # 循环遍历字符串的每一个字符
        # for i in range(str_length):
        #     # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
        #     if i - max_length >= 1 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1]:
        #         # 记录当前开始位置
        #         start = i - max_length - 1
        #         # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
        #         max_length += 2
        #         continue
        #     # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
        #     if i - max_length >= 0 and s[i-max_length: i+1] == s[i-max_length: i+1][::-1]:
        #         start = i - max_length
        #         # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
        #         max_length += 1
        # # 返回最长回文子串
        # return s[start: start + max_length]
        
        ### 中心扩散：选取一个中心点向两边扩散并判断是否为回文，并记录所有搜索到的最长回文并返回结果
        if len(s) < 2 or s == s[::-1]:
            return s
        start = 0
        maxlen = 1
        for i in range(1, len(s)):
            odd = s[i - maxlen - 1 : i + 1]
            even = s[i - maxlen : i + 1]
            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start : start + maxlen]