'''
**************************************************************************************************************************
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            # 如果这里仅判断if matrix，那么对于测试数组例[[1],[2],[3]]，循环后变成了[[],[]]，matrix不为空
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                # 左边界即为数组从尾到头的每一项子数组的第一个元素
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

# Solution 2
# https://www.jianshu.com/p/34a4097f57e5
# 主要思想为遍历第一行，然后删除第一行，再逆时针旋转矩阵，循环。代码简洁明了。
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix:
                break
            # 对矩阵逆时针旋转，详情见上面网址
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res

# 还有种逆时针旋转矩阵的方法，先转置再取反
    def turn(self, matrix):
        res = []
        for j in range(len(matrix[0])):
            tmp = []
            for i in range(len(matrix)):
                tmp.append(matrix[i][j])
            res.append(tmp)
        res.reverse()
        return res

    # solution 3
    def aa(matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        ret=[]
        while start*2 <rows and start*2<cols:
            bb(matrix,rows,cols,start,ret)
            start +=1
            
        return ret


    def bb(matrix,rows,cols,start,ret):
        row=rows-start-1
        col=cols-start-1
        
        for c in range(start,col+1):
            ret.append(matrix[start][c])
            
        if start <row:
            for r in range(start+1,row+1):
                ret.append(matrix[r][col])
                
        if start <row and start<col:
            for c in range(start,col)[::-1]:
                ret.append(matrix[row][c])
                
        if start <row and start<col:
            for r in range(start+1,row)[::-1]:
                ret.append(matrix[r][start])