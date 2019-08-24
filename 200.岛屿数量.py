'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 输入是字符串
        if not grid:
            return 0
        w = len(grid[0])
        h = len(grid)
        # 在图的外侧添一圈‘0’
        new_grid = [['0' for _ in range(w + 2)]]
        for g in grid:
            new_grid.append(['0'] + g + ['0'])
        new_grid.append(['0' for _ in range(w + 2)])
        num = 0
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if new_grid[i][j] == '1':
                    num += 1
                    self.deepsearch(i, j, new_grid)
        return num
    
    def deepsearch(self, i, j, grid):
        if grid[i][j] == '0':
            return
        # 如果当前是陆地，把当前结点标记遍历过，并分别看左右上下四个位置
        grid[i][j] = '0'
        self.deepsearch(i - 1, j, grid)
        self.deepsearch(i + 1, j, grid)
        self.deepsearch(i, j - 1, grid)
        self.deepsearch(i, j + 1, grid)