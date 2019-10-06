'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'              
    
    def dfs(self, board, i, j):
        board[i][j] = '*'
        if i - 1 >= 0 and board[i - 1][j] == 'O':
            self.dfs(board, i - 1, j)
        if i + 1 <= len(board) - 1 and board[i + 1][j] == 'O':
            self.dfs(board, i + 1, j)
        if j - 1 >= 0 and board[i][j - 1] == 'O':
            self.dfs(board, i, j - 1)
        if j + 1 <= len(board[0]) - 1 and board[i][j + 1] == 'O':
            self.dfs(board, i, j + 1)
    
    # DFS还有一种写法
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '*'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)