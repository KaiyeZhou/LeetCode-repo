class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 优化后的动态规划，因为只需考虑上一个数的情况，不需要记录前面所有的值
        max_sum = nums[0]
        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum < 0:
                pre_sum = nums[i]
            else:
                pre_sum = pre_sum + nums[i]
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum
        
        # 2
        # n = len(nums)
        # for i in range(1, n):
        #     nums[i] = max(nums[i-1] + nums[i], nums[i])
        # return max(nums)

        # 原始的动态规划
        n = len(nums)
        res = nums[0]
        dp = [nums[0]] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res