'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons

https://blog.csdn.net/XX_123_1_RJ/article/details/81638353
https://segmentfault.com/a/1190000018191476
https://blog.csdn.net/u014626513/article/details/81146851
https://blog.csdn.net/qq_37369124/article/details/88264797
假设 nums[-1] = nums[n] = 1（在开始和结尾添加一个值为1的气球）
动态规划，建立数组dp
dp[a][c]表示戳破第a+1到c-1个气球能获得的最大值，
在第a到c个中最后戳破第b个气球获得的硬币最大值 dp[a][b] + dp[b][c] +nums[a] * nums[b]* nums[c]
统计b的所有可能，比较出 dp[a][c]的最大值
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(2, n):
            for j in range(n - i):
                for k in range(j + 1, j + i):
                    dp[j][j + i] = max(dp[j][j + i], dp[j][k] + dp[k][j + i] + nums[j] * nums[k] * nums[j + i])
        return dp[0][-1]

        # 说明
        nums = [1] + [i for i in nums if i > 0] + [1]  # 清除为0的数字，因为0不会得分，然后首尾添加[1],方便计算
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # 初始化dp
        for k in range(2, n):  # k 确定一个滑动窗口的大小，从2开始
            for left in range(0, n - k):  # 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
                right = left + k
                for i in range(left + 1, right):  # 开始枚举，区间内哪一个数字作为最后一个被戳破，使其得分最高
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]