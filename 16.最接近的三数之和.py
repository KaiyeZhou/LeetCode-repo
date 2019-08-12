'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # res = []
        # # res1 = []
        # for i in range(len(nums)-2):
        #     j = i + 1
        #     k = len(nums) - 1
        #     while j < k:
        #         if nums[i] + nums[j] + nums[k] == target:
        #             return nums[i] + nums[j] + nums[k]
        #         if nums[i] + nums[j] + nums[k] > target:
        #             res.append(nums[i] + nums[j] + nums[k])
        #             k -= 1
        #         if nums[i] + nums[j] + nums[k] < target:
        #             res.append(nums[i] + nums[j] + nums[k])
        #             j += 1
        # res.sort(key=lambda x:abs(x-target))
        # return res[0]
        
        # 2
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i] + nums[j] + nums[k]
                elif nums[i] + nums[j] + nums[k] > target:
                    res.append(nums[i] + nums[j] + nums[k])
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    res.append(nums[i] + nums[j] + nums[k])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        res.sort(key=lambda x:abs(x-target))
        return res[0]
            
        # 3    *********
        res = []
        n = len(nums)
        nums = sorted(nums)
        for k in range(n-2):
            i,j = k+1,n-1
            if  nums[i]+nums[k]+nums[i+1] > target:        # 当前k下，最小的和
                res.append(nums[i]+nums[k]+nums[i+1])
            elif nums[j]+nums[j-1]+nums[k] <target:        # 当前k下，最大的和
                res.append(nums[j]+nums[k]+nums[j-1])
            else:
                while i<j:
                    if nums[i]+nums[k]+nums[j]==target:
                        return target
                    elif nums[i]+nums[k]+nums[j]>target:
                        res.append(nums[i]+nums[k]+nums[j])
                        j-=1
                        while i < j and nums[j] == nums[j + 1]: j -= 1
                    else:
                        res.append(nums[i]+nums[k]+nums[j])
                        i+=1
                        while i < j and nums[i] == nums[i - 1]: i += 1

        res.sort(key=lambda x:abs(x-target))
        return res[0]
        
        # 4
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            min_value = nums[i] + nums[left] + nums[left + 1]
            if min_value > target:
                if abs(min_value-target) < abs(closest-target):
                    closest = min_value
                break
            
            max_value = nums[i] + nums[right] + nums[right - 1]
            if max_value < target:
                if abs(max_value-target) < abs(closest-target):
                    closest = max_value
                continue
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(total-target) < abs(closest-target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
        return closest