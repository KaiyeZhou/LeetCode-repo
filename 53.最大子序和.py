class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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