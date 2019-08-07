'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num, path):
            if not num:
                res.append(path)
                return
            for i in range(len(num)):
                dfs(num[:i] + num[i+1:], path + [num[i]])
        
        res = []
        dfs(nums, [])
        return res