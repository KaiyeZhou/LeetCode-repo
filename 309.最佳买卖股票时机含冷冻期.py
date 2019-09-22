'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# https://blog.csdn.net/Languedoc_Roussillon/article/details/100736388
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        buy = [0 for _ in range(n)]
        sale = [0 for _ in range(n)]
        cool = [0 for _ in range(n)]
        buy[0] = -prices[0]
        for i in range(1, n):
            cool[i] = sale[i - 1]      # 冷冻期的上一个状态一定是卖出
            buy[i] = max(buy[i - 1], cool[i - 1] - prices[i])   # 如果今天买入就是用上一次冷冻期的价格减去当天的股票交易,如果此次不买入，则价格就为上一次的买入价格
            sale[i] = max(sale[i - 1], buy[i - 1] + prices[i]) # 在sale[i-1]之前卖出了或者sale[i]的时候卖出，就是考虑当天是否要或者可以卖出
        return max(sale[n - 1], cool[n - 1])

        # solution 2
        # https://blog.csdn.net/qq_36309480/article/details/88134706
        if not prices:
            return 0
        sell = [0]*len(prices)  # sell[i]代表在第i天手里没有股票情况下的最大利润，令hold[i]代表在第i天手里有股票情况下的最大利润
        hold = [0]*len(prices)
        hold[0] = -prices[0]
        for i in range(1,len(prices)):
            sell[i] = max(sell[i-1],hold[i-1]+prices[i])
            hold[i] = max(hold[i-1],(sell[i-2] if i>=2 else 0) -prices[i])
        return sell[-1]