class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num not in dict_1:
                dict_1[nums[i]] = i
            else:
                return [dict_1[num], i]