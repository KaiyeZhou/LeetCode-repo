# https://blog.csdn.net/fuxuemingzhu/article/details/79433960

class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        count = 0
        for i in range(0, l - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right < l:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
            left = i
            right = i + 1
            while left >= 0 and right < l:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count + l
        
        ## 动态规划
        # l = len(s)
        # count = 0
        # tmp = [[False] * l for _ in range(l)]
        # ### 单个字符
        # for i in range(l):
        #     tmp[i][i] = True
        #     count += 1
        # ### 两个字符是回文
        # for i in range(1, l):
        #     if s[i - 1] == s[i]:
        #         tmp[i - 1][i] = True
        #         count += 1
        # ### 多个字符
        # for j in range(1, l):
        #     for i in range(j - 1):
        #         if s[i] == s[j] and tmp[i + 1][j - 1]:
        #             tmp[i][j] = True
        #             count += 1
        # return count
        
        ##以某个字符为中心向两边扩展，最大的扩展宽度就是以该字符为中心的回文子串的个数。所有位置上的回文子串的个数就是字符串中奇数回文子串的个数。要想求偶数，可以在每个字符之间插入特殊字符如@， 这样再按上述做法得到的结果就是全部的回文子串的个数。其中要注意子串边界为特殊字符的子串不应记录在内。
        # s = '@'.join([i for i in s])
        # N = len(s)
        # res = 0
        # for i in range(N):
        #     j = 0
        #     while j <= min(i, N - 1 - i) and s[i - j] == s[i + j]:
        #         res += s[i - j] != '@'
        #         j += 1
        # return res

                