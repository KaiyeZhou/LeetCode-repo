class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i]表示到第i-1位时解码的方法数
        dp = [0] * (n + 1)
        # 状态转移：dp[i] = dp[i - 1] + (dp[i - 2] if 双字符合格 else 0)
        if s[0] != '0':
            dp[0] = 1
            dp[1] = 1
        else:
            return 0 
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if 9 < int(s[i - 2 : i]) < 27:
                dp[i] += dp[i - 2]
        return dp[-1]