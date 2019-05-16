# https://blog.csdn.net/fuxuemingzhu/article/details/79367789
# 从1...n中找出一个i作为根节点，比i小的数1...i-1作为左子树，比i大的数i+1...n作为右子树，左子树的排列和右子树的排列的乘积是此时的数目。

class Solution:
    def numTrees(self, n: int) -> int:
        ## 记忆化递归
        # dp = dict()
        # if n in dp:
        #     return dp[n]
        # if n == 0 or n == 1:
        #     return 1
        # ans = 0
        # for i in range(1, n + 1):
        #     ans += self.numTrees(i - 1) * self.numTrees(n - i)
        # dp[n] = ans
        # return ans
        
        ## 动态规划
        dp = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):              ###左子树有j个节点
                count += dp[j] * dp[i - j -1]
            dp.append(count)
        return dp[-1]
        
        ## 卡特兰数
        