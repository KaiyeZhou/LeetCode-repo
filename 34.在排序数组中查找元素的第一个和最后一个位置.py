class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        flag = 0
        for i in range(len(nums)):
            if flag == 0 and nums[i] == target:
                res[0] = i
                flag = 1
            if flag == 1 and nums[i] == target:
                res[1] = i
        if res[1] == -1:
            res[1] = res[0]
            return res
        else:
            return res

        # 方法二
        def directSearch(nums,key):
            for i in range(len(nums)):
                if nums[i]==key:
                    return i
            return [-1,-1]
        tmp=directSearch(nums,target)
        if tmp==[-1,-1]:
            return tmp
        a=nums.count(nums[tmp])
        return [tmp,tmp+a-1]