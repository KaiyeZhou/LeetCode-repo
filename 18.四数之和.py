'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        # res = []
        # if len(nums) < 4:
        #     return res
        # for i in range(len(nums) - 3):
        #     if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
        #         continue
        #     for j in range(i + 1, len(nums) - 2):
        #         if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
        #             continue
        #         x = j + 1
        #         y = len(nums) - 1
        #         while x < y:
        #             if nums[i] + nums[j] + nums[x] + nums[y] == target:
        #                 res.append([nums[i], nums[j], nums[x], nums[y]])
        #                 x += 1
        #                 while x < y and nums[x] == nums[x - 1]:
        #                     x += 1
        #             elif nums[i] + nums[j] + nums[x] + nums[y] < target:
        #                 x += 1
        #             else:
        #                 y = y - 1
        # rr = []
        # for r in res:
        #     if r not in rr:
        #         rr.append(r)
        # return rr
        
        # 2
        dic = {}
        nums.sort()
        res = set()
        # 先计算前两个数之和
        for i in range(len(nums) - 1):
            for p in range(i + 1, len(nums)):
                key = nums[i] + nums[p]
                if key not in dic:
                    dic[key] = [(i, p)]
                else:
                    dic[key].append((i, p))
        
        for i in range(2, len(nums) - 1):
            for p in range(i + 1, len(nums)):
                pre = target - nums[i] - nums[p]
                if pre in dic:
                    for index in dic[pre]:
                        if index[1] < i:
                            res.add((nums[index[0]], nums[index[1]], nums[i], nums[p]))
        return [list(i) for i in res]