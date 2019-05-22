class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## 超时了。。。
        # res = []
        # l = len(height)
        # for i in range(l):
        #     for j in range(i+1, l):
        #         product = (j - i) * min(height[i], height[j])
        #         res.append(product)
        # return max(res)
        
        ### 贪心算法  移动矮的一边
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1
        # res = (right - left) * min(height[left], height[right])
        res = 0
        while left < right:
            if height[left] < height[right]:
                if res < (right - left) * height[left]:
                    res = (right - left) * height[left]
                left += 1
            else:
                if res < (right - left) * height[right]:
                    res = (right - left) * height[right]
                right -= 1
        return res
        
        ###
#         l = 0
#         r = len(height)-1
#         if not height or len(height) == 1 :
#             return 0
#         res = (r-l)*(height[l] if height[l] < height[r] else height[r])
        
#         while l < r:
#             if height[l] < height[r] :
#                 res = res if res > height[l]*(r-l) else height[l]*(r-l)
#                 l += 1
#             else :
#                 res = res if res > height[r]*(r-l) else height[r]*(r-l) 
#                 r -=1
#         return res
