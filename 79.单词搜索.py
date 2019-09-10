'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            tmp = board[i][j]
            board[i][j] = '#'
            if i - 1 >= 0 and board[i - 1][j] == word[0] and dfs(board, i - 1, j, word[1:]):
                return True
            if i + 1 <= len(board) - 1 and board[i + 1][j] == word[0] and dfs(board, i + 1, j, word[1:]):
                return True
            if j - 1 >= 0 and board[i][j - 1] == word[0] and dfs(board, i, j - 1, word[1:]):
                return True
            if j + 1 <= len(board[0]) - 1 and board[i][j + 1] == word[0] and dfs(board, i, j + 1, word[1:]):
                return True 
            board[i][j] = tmp
            return False
        
        if not board or not board[0] or len(word) == 0:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, word[1:]):
                        return True
        return False
    
# solution 2
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #深搜解法
        if not board:
            return False
        #搜索可能的起始位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,i,j):
                    return True
        return False
 
    def dfs(self,board,word,i,j):
        #dfs终止条件
        if len(word) == 0:
            return True
        #边界终止条件
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        #不能搜索到之前的位置，设该位置为None
        tmp,board[i][j] = board[i][j],None
        #向上下左右四个方向搜索
        res = self.dfs(board,word[1:],i-1,j) or self.dfs(board,word[1:],i+1,j) or self.dfs(board,word[1:],i,j-1) or self.dfs(board,word[1:],i,j+1)
        board[i][j] = tmp
        return res

# wrong
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not board[0] or len(word) == 0:
#             return False
#         m = len(board)
#         n = len(board[0])
#         visited = [[0] * n] * m
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0]:
#                     res = 0                    
#                     res = self.dfs(board, i, j, word[1:], 0, visited)                 
#                     if res == len(word):
#                         return True
#         return False
    
#     def dfs(self, board, i, j, word, res, visited):
#         visited[i][j] = 1
#         res += 1
#         if len(word) == 0:
#             return res
#         if i + 1 <= len(board) - 1 and visited[i + 1][j] == 0 and board[i + 1][j] == word[0]:
#             res = self.dfs(board, i + 1, j, word[1:], res, visited)
#         if i - 1 >= 0 and visited[i - 1][j] == 0 and board[i - 1][j] == word[0]:
#             res = self.dfs(board, i - 1, j, word[1:], res, visited)
#         if j + 1 <= len(board[0]) - 1 and visited[i][j + 1] == 0 and board[i][j + 1] == word[0]:
#             res = self.dfs(board, i, j + 1, word[1:], res, visited)
#         if j - 1 >= 0 and visited[i][j - 1] == 0 and board[i][j - 1] == word[0]:
#             res = self.dfs(board, i, j - 1, word[1:], res, visited)
#         visited[i][j] = 0
#         return res