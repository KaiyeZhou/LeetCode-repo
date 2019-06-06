class Solution:
    def minCut(self, s: str) -> int:
        # if len(s) == 0 or s == s[::-1]:
        #     return 0
        # res = [i for i in range(-1, len(s))]
        # judge = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]
        # for i in range(1, len(s) + 1):
        #     for j in range(i):
        #         if s[i - 1] == s[j] and (i - j <= 2 or judge[j + 1][i - 1]):
        #             judge[j][i] = True
        #             res[i] = min(res[j] + 1, res[i])
        # return res[-1]
        
        ###2
        # if not s or s == s[::-1]: 
        #     return 0
        # n = len(s)
        # for i in range(1, n):
        #     if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
        #         return 1
        # dp = list(range(-1, n))
        # for i in range(n):
        #     for k in range(0, min(n - i, i + 1)):
        #         if s[i + k] != s[i - k]:
        #             break
        #         dp[i + k + 1] = min(dp[i + k + 1], dp[i - k] + 1)
        #     for k in range(1, min(n - i, i + 2)):    
        #         if s[i + k] != s[i - k + 1]:
        #             break
        #         dp[i + k + 1] = min(dp[i + k + 1], dp[i - k + 1] + 1)
        # return dp[n]
        
        ### 3
        #回文有两种情况字符数为奇数或偶数个，如‘aba’和‘bb’
        if s == s[::-1]: return 0
        for i in range(1,len(s)):
            if s[i:] == s[:i-1:-1] and s[:i] == s[i-1::-1]: return 1
        dp = []
        for i in range(-1,len(s)):
            dp.append(i)
        for i in range(len(s)):
            t=0
            while i-t >=0 and i+t<len(s) and s[i-t]==s[i+t]:
                dp[i+t+1]= min(dp[i+t+1], dp[i-t] + 1)
                t=t+1
            t=0
            while i-t>=0  and i+t+1<len(s) and s[i-t]==s[i+t+1]:
                dp[i+t+2] = min(dp[i+t+2], dp[i-t]+1)
                t=t+1
        return dp[-1]
