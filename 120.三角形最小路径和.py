class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:             
        # 从底层往上层计算，利用动态规划
        res = triangle[-1]
        # 获得倒数第二层列表的索引位置
        i = len(triangle) - 2
        while i >= 0:
            for j in range(len(triangle[i])):
                #选择最小的元素和上层元素相加，同时更新列表
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
            i -= 1
        return res[0]