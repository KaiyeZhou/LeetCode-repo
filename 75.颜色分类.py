'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 计数排序
        tmp = [0, 0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp[0] += 1
            if nums[i] == 1:
                tmp[1] += 1
            if nums[i] == 2:
                tmp[2] += 1
        for i in range(tmp[0]):
            nums[i] = 0
        for i in range(tmp[0], tmp[0] + tmp[1]):
            nums[i] = 1
        for i in range(tmp[0] + tmp[1], len(nums)):
            nums[i] = 2
        return 

        # 三指针排序
        right = len(nums) - 1
        left = middle = 0
        while middle <= right:
            if nums[middle] == 2:
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
            elif nums[middle] == 0:
                nums[middle], nums[left] = nums[left], nums[middle]
                middle += 1
                left += 1
            else:
                middle += 1
        return

        # 3
        right = len(nums) - 1
        left = middle = 0
        while middle <= right:
            if nums[middle] == 2:
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
            elif nums[middle] == 0:
                # nums[middle], nums[left] = nums[left], nums[middle]
                nums[left] = 0
                if middle > left:
                    nums[middle] = 1
                middle += 1
                left += 1
            else:
                middle += 1
        return