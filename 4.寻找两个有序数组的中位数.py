class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # numList = nums1 + nums2
        # numList.sort()
        # if len(numList) % 2 == 0:
        #     return (float(numList[int(len(numList) / 2)]) + numList[int(len(numList) / 2 - 1)]) / 2
        # res = numList[int(len(numList) / 2)]
        # return float(res)
        
        ##
        # nums1.extend(nums2)
        # nums1.sort()
        # L = len(nums1)
        # if L%2==0:
        #     return float((nums1[L//2-1]+nums1[L//2])/2)
        # else:
        #     return float(nums1[(L+1)//2-1])
        
        ###
        # n&1 与运算
        # if n&1可以判断n是否为偶数
        # 如果是偶数，n&1返回0；否则返回1
        
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2==0:
            return float((nums[(n-1)//2]+nums[n//2])/2)
        else:
            return float(nums[n//2])