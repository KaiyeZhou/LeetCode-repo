class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        res += d[s[len(s) - 1]]
        if 1 <= res <= 3999:
            return res
    
        # # 使用整数转罗马数的两个列表
        # num_tuple = [1000, 500, 100, 50, 10, 5, 1]
        # roman_tuple = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        # # 使用dict和zip方法是其转为字典 格式为：{'M': 1000, 'X': 10, 'L': 50, 'D': 500, 'C': 100, 'V': 5, 'I': 1}
        # merge_dic = dict(zip(roman_tuple, num_tuple))
