'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 用前缀和数组
        from collections import defaultdict
        pre_sum = 0
        record = defaultdict(int)
        record[0] = 1
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            res += record[pre_sum - k]
            record[pre_sum] += 1
        return res

        # 可能超时
        res = 0
        for i in range(len(nums)):
            pre_sum = 0
            for j in range(i, len(nums)):
                pre_sum += nums[j]
                if pre_sum == k:
                    res += 1
        return res

        # 换一种写法
        dic = {0:1}
        res = 0
        pre_sum = 0
        for i in nums:
            pre_sum += i
            if pre_sum - k in dic:
                res += dic[pre_sum - k]
            if pre_sum in dic:
                dic[pre_sum] += 1
            else:
                dic[pre_sum] = 1
        return res