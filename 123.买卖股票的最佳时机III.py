'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        local = [[0] * 3 for _ in range(n)]    # 定义local[i][j]为在到第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，为局部最优
        globa = [[0] * 3 for _ in range(n)]    # 定义globa[i][j]为在到第i天时最多可进行j次交易的最大利润，为全局最优
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            for j in range(1, 3):
                local[i][j] = max(globa[i-1][j-1], local[i-1][j]) + diff  #局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值中取较大值
                globa[i][j] = max(globa[i-1][j], local[i][j])  #全局最优比较局部最优和前一天的全局最优。
        return globa[n-1][2]

        # solution2
        if not prices:
            return 0
        # s1是假设第一天就买入股票，s2，s3，s4则分别设为最小值
        s1 = -prices[0]
        s2, s3, s4 = float('-inf'), float('-inf'), float('-inf')
        for i in range(len(prices)):
            s1 = max(s1, -prices[i])      #在该天第一次买入股票可获得的最大收益 （手上的钱）
            s2 = max(s2, s1 + prices[i])  #在该天第一次卖出股票可获得的最大收益（手上的钱）
            s3 = max(s3, s2 - prices[i])  #在该天第二次买入股票可获得的最大收益（手上的钱）
            s4 = max(s4, s3 + prices[i])  #在该天第二次卖出股票可获得的最大收益（手上的钱）
        return max(0, s4)

        # solution3
        # https://blog.csdn.net/ggdhs/article/details/92618827