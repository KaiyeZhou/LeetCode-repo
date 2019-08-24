'''
输出所有最长递增子序列，考虑长度相等的最长子序列
'''
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
n = len(nums)
m = [1] * n                                                #m[x]中存着nums中0-x项中递增子序列的长度

for x in range(1,n):                                    
    for y in range (0,x):                             #nums
        if nums[x] > nums[y] and m[x] <= m[y]:    # 计算m的x项 ，更新m的0～x-1项
            m[x] += 1

    subseq = []                                        
    max_value = max(m)

    for i in range(n-1,-1,-1):                    #获取0-x项递增子序列
        if m[i] == max_value:
            subseq.append(nums[i])
            max_value -= 1
    subseq.reverse()
print(subseq)

#### 没有输出所有的最长子序列