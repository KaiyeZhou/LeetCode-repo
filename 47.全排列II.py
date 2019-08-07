'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         def dfs(num, path):
#             if not num:
#                 if path in res:
#                     return
#                 else:
#                     res.append(path)
#                     return
#             for i in range(len(num)):
#                 dfs(num[:i] + num[i + 1:], path + [num[i]])
        
#         res = []
#         dfs(nums, [])
#         return res

    # 速度更快，   
        nums.sort()
        res=[]
        self.gen(nums,[],res)
        return res
    
    def gen(self,nums,sol,res):
        if not nums:
            res.append(sol)
            return
        for i,n in enumerate(nums):
            if i and n==nums[i-1]:
                continue
            self.gen(nums[:i]+nums[i+1:],sol+[n],res)