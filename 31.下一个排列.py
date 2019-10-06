'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.sort()   # 不能用nums = nums[::-1] ，这样会改变nums的id号，不满足原地修改数组条件
            # print(id(nums))
            return
        j = i - 1
        while i < len(nums) - 1 and nums[i + 1] > nums[j]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[j+1:] = sorted(nums[j+1:])

S = Solution()
nums = [3,2,1]
S.nextPermutation(nums)
print(id(nums))