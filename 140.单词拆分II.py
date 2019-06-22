# https://blog.csdn.net/weixin_42771166/article/details/85567953

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        if len(s) == 0 or not wordDict:
            return []
        strides = [len(x) for x in wordDict]
        max_strides = max(strides)
        stride_set = set(strides)
        # 判断能不能拆分，用到单词拆分I的解答
        if self.canBreak(s, wordDict):
            self.sub_wordBreak(s, wordDict, stride_set, [], res)
        return res
    
    def canBreak(self, s, wordDict):
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            if dp[i]:
                for j in range(i, n):
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]
    
    def sub_wordBreak(self, sub_s, wordDict, stride_set, cur_result, result):
        if len(sub_s) == 0:
            result.append(' '.join(cur_result))
        else:
            for stride_length in stride_set:
                if stride_length <= len(sub_s):
                    if sub_s[:stride_length] in wordDict:
                        self.sub_wordBreak(sub_s[stride_length:], wordDict, stride_set, cur_result + [sub_s[:stride_length]], result)