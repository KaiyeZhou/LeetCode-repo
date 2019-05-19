class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1:
        #     return s
        # rows = [''] * min(numRows, len(s))
        # godown = False
        # currow = 0
        # for c in s:
        #     rows[currow] += c
        #     if currow == 0 or currow == numRows - 1:
        #         godown = not godown
        #     if godown:
        #         currow += 1
        #     else:
        #         currow -= 1
        # return ''.join(rows)    # 把列表变成字符串
        
        ##找出数字索引与行列数的关系
        if numRows == 1:
            return s
        ans = ''
        interval = 2 * numRows - 2
        ans += s[::interval]                   
        for i in range(1, numRows - 1):
            innergap = interval - 2 * i
            for j in range(i, len(s), interval):
                ans += s[j]
                if j + innergap < len(s):
                    ans += s[j + innergap]
        ans += s[numRows - 1 :: interval]
        return ans