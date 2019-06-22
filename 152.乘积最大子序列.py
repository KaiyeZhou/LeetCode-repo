class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 乘积子数组中可能有负数，所以要同时考虑最大乘积和最小乘积
        n = len(nums)
        res = nums[0]
        dp_max = [nums[0]] * n
        dp_min = [nums[0]] * n
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res