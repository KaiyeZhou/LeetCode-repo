class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ## 递归
        # 用i遍历数组各个位置，如果s[:i]为回文串，则对后半部分进行递归，将返回的结果中每一项加上s[:i]并将该项添加至最终结果
        # if s == '':
        #     return []
        # res = []
        # if s == s[::-1]:
        #     res.append([s])
        # for i in range(len(s)):
        #     if s[:i+1] == s[i::-1]:
        #         p = self.partition(s[i+1:])
        #         for c in p:
        #             if c != []:
        #                 res.append([s[:i+1]] + c)
        # return res
        
        ## 
        # res = []
        # def dfs(start, tmp):
        #     if start >= len(s):
        #         res.append(tmp[:])
        #     for i in range(start, len(s)):
        #         substring = s[start:i + 1]
        #         if substring == substring[::-1]:  #子串是回文串
        #             tmp.append(substring)
        #             dfs(i + 1, tmp)
        #             tmp.pop()
        # dfs(0, list())
        # return res
        
        '''
        注意其中的回溯逻辑：只需要判断前一个或者两个即可
        动态生成的过程，保证了前一组循环保留了其前面一组所有可能的回文子串，则只需要依次判断即可
        '''
        if not s:
            return []
        res = [[]]
        for i, x in enumerate(s):
            tmp = []
            for r in res:
                tmp.append(r + [x])
                if len(r) >= 1 and r[-1] == x:
                    tmp.append(r[:-1] + [r[-1] + x])
                if len(r) >= 2 and r[-2] == x:
                    tmp.append(r[:-2] + [r[-2] + r[-1] + x])
            res = tmp
        return res