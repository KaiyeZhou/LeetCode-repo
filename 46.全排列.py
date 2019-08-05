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