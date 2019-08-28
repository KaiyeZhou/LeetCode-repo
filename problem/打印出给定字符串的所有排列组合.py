'''
给你一个字符串，比如‘abc’，请打印出该字符串的所有排列组合：
以‘abc’为例，输出的结果应该是：'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
'''

def helper(s):
    if len(s) <= 1:     # 递归出口：长度为1的字符串，其排列组合就是它本身
        return [s]
    sl = []             # 保存字符串的所有可能排列组合
    for i in range(len(s)):     # 确定字符串的第一个字母，有n中可能，n为字符串s的长度
        for j in helper(s[0:i] + s[i + 1:]):    # 进入递归，返回第一个字符+除去第一个字符外的字符串的排列组合
            sl.append(s[i] + j)
    return sl

s = 'abc'     # 如果存在字符相同的情况，要去重
# nums = list(set(nums))
nums = helper(s)    
print(nums)