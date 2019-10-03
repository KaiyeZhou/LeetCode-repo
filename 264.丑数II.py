'''
编写一个程序，找出第 n 个丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。
示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  
1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        id2, id3, id5 = 0, 0, 0
        for i in range(1, n):
            res.append(min(res[id2] * 2, res[id3] * 3, res[id5] * 5))
            if res[i] == res[id2] * 2:
                id2 += 1
            if res[i] == res[id3] * 3:
                id3 += 1
            if res[i] == res[id5] * 5:
                id5 += 1
        return res[n - 1]