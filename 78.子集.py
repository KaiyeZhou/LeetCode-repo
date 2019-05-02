class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## 中间变量法
        # res = [[]]
        # for num in nums:
        #     for tmp in res[:]:  ## 深拷贝和浅拷贝
        #         x = tmp[:]
        #         x.append(num)
        #         res.append(x)
        # return res
        
        ### 回溯
#         res = []
#         tmp = []
        
#         def dfs(nums, res, start, tmp):
#             x = tmp[:]
#             res.append(x)       #深拷贝与浅拷贝的问题，分片操作对多维数组来说也是浅拷贝啊
#             for i in range(start, len(nums)):
#                 tmp.append(nums[i])  #添加第i个元素
#                 dfs(nums, res, i + 1, tmp)
#                 tmp.remove(nums[i])
        
#         dfs(nums, res, 0, tmp)
#         return res
        
        ### 回溯2
        # res = []
        # def dfs(nums, tmp, start):
        #     res.append(tmp[:])
        #     for i in range(start, len(nums)):
        #         tmp.append(nums[i])
        #         dfs(nums, tmp, i + 1)
        #         tmp.pop()
        # dfs(nums, [], 0)
        # return res
        
        ## 动态规划的方法（之后回过来看）
        result = self.subset_func(nums)  
        for line in result:  
            line.sort()  
        return result  
          
    def subset_func(self,nums):  
        if len(nums)==0:  
            return [[]]  
        if len(nums)==1:  
            return [[],nums]  
        first = nums[0]  
        tmp_nums = nums[1:]  
        tmp_result = self.subset_func(tmp_nums)  
        result = []  
        for key in tmp_result:  #动态规划的方法，result包括tmp_result的所有的，还包括tep_result都加上first
            result.append(key)  
            tmp = list(key)  
            tmp.append(first)  
            result.append(tmp)  
        return result
