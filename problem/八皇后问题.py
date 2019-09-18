'''
问题： 国际象棋棋盘是8 * 8的方格，每个方格里放一个棋子。皇后这种棋子可以攻击同一行或者同一列或者斜线（左上左下右上右下四个方向）上的棋子。
在一个棋盘上如果要放八个皇后，使得她们互相之间不能攻击（即任意两两之间都不同行不同列不同斜线），求出一种（进一步的，所有）布局方式。

***************https://www.cnblogs.com/franknihao/p/9416145.html************
'''

def check(board, pos):
    x, y = pos
    blen = len(board)
    for i in range(x):
        for j in range(blen):
            if board[i][j] == 1:
                if j == y or abs(j - y) == abs(x - i):
                    return False
    return True

def EightQueen(board, row):
    blen = len(board)
    if row == blen:           # 来到不存在的第九行（假设共八行八列）
        print(board)
        return True
    for possibleY in range(blen):
        if check(board, (row, possibleY)):
            board[row][possibleY] = 1            # 放置一个Queen
            if not EightQueen(board, row + 1):    # 这里其实是本行下面所有行放置皇后的入口，但是如果最终这条路没有找到一个解，那么
                board[row][possibleY] = 0         # 应该将刚才放置的皇后收回，再去寻找下一个可能发生的解
            else:
                return True
    return False

## 不创建二维数组，用一维数组,下标本身就代表了board中的某一行，然后值是指这一行中皇后放在第几列。
def check(board,row,col):
    i = 0
    while i < row:
        if abs(col-board[i]) in (0,abs(row-i)):    # 这是元组，等于0或者是abs(row-i)
            return False
        i += 1
    return True

def EightQueen(board,row):
    blen = len(board)
    if row == blen:    # 来到不存在的第九行了
        print(board)
        return True
    col = 0
    while col < blen:
        if check(board,row,col):
            board[row] = col
            if EightQueen(board,row+1):
                # return True                  # 去掉这里加上pass即可，或者直接删除掉整个判断，只留下单一个EightQueen(board,row+1)
                pass
        col += 1
    return False


blen = 8
board = [[0 for j in range(blen)] for i in range(blen)]
EightQueen(board, 0)