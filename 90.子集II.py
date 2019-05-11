class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for tmp in res[:]:
                x = tmp[:]
                x.append(num)
                y = sorted(x)
                if y not in res[:]:
                    res.append(y)
        return res
        
        ###
        # nums.sort()
        # result = [[]]
        # for num in nums:
        #     for i in result[:]:
        #         item = i[:]
        #         item.append(num)
        #         if item not in result:
        #             result.append(item[:])
        # return result
     
        ###
    #     #先排序
    #     nums.sort()
    #     self.res = []
    #     self.dfs([], 0, nums)
    #     return self.res
    # def dfs(self, temp, j, nums):
    #     self.res.append(temp[:])
    #     for i in range(j, len(nums)):
    #         #跳过重复
    #         if i > j and nums[i] == nums[i-1]:
    #             continue
    #         temp.append(nums[i])
    #         self.dfs(temp, i+1, nums)
    #         temp.pop()
    #     return
                    
                