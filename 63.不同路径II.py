'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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