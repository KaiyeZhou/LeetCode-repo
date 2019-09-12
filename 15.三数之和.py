'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a+b+c = 0 等价于 a+b = -c
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res

# 2222
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import bisect
        ans=[]
        counts={}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        nums=sorted(counts)
        for i,num in enumerate(nums):
            if counts[num]>1:
                if num==0:
                    if counts[num]>2:
                        ans.append([0,0,0])
                else:
                    if -num*2 in nums:
                        ans.append([num,num,-2*num])
            if num<0:
                twosum=-num
                left=bisect.bisect_left(nums,(twosum-nums[-1]),i+1)
                for i in nums[left:bisect.bisect_right(nums,(twosum//2),left)]:
                    j=twosum-i
                    if j in counts and j!=i:
                        ans.append([num,i,j])
        return ans