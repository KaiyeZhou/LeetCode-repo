'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长, 则递推式为: 
        # dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)      # 行
        n = len(matrix[0])   # 列
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0        # 正方形最大边长
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
        return ans * ans