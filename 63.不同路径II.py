class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        #     return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[0][j] = dp[0][j - 1]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]