'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # dp[i][j]表示到第i行第j列位置，总共有多少条不同路径
        # dp = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         # 递推公式
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]
        
        ## 
        #dp[i][j]表示到第i行j列为止总共有多少条不同的路径
        # dp = [[0 for _ in range(n)]for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         #初始条件
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             #递推公式
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]
        
        ## 组合问题
        # C^(m-1)_(m+n-2)
        res = 1
        for i in range(m, m+n-1):
            res *= i
            res /= i-m+1
        return int(res)