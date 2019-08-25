'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w = len(grid[0])
        h = len(grid)
        res = 0
        area = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    area = self.DFS(grid, i, j, area)
                    res = max(res, area)
                    area = 0
        return res
    
    def DFS(self, grid, i, j, area):
        grid[i][j] = 2
        area += 1
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            area = self.DFS(grid, i - 1, j, area)
        if i + 1 <= len(grid) - 1 and grid[i + 1][j] == 1:
            area = self.DFS(grid, i + 1, j, area)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            area = self.DFS(grid, i, j - 1, area)
        if j + 1 <= len(grid[0]) - 1 and grid[i][j + 1] == 1:
            area = self.DFS(grid, i, j + 1, area)
        return area