'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 从左上角开始遍历数组，将grid（数组）内容存储为走到当前位置的最短路径和，故只考虑当前位置的上边和左边哪个小
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                    continue
                if i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                    continue
                if i != 0 and j != 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                    continue
        return grid[m - 1][n - 1]
        
        ## 2
        # if not grid:
        #     return 0
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp [i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-1][-1]