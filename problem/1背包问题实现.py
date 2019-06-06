'''
给定一组多个（n）物品，每种物品都有自己的重量（wi w_iw 
i
​	
 ）和价值（vi v_iv 
i
​	
 ），在限定的总重量/总容量（C）内，选择其中若干个（也即每种物品可以选0个或1个），设计选择方案使得物品的总价值最高。

思路：
定义问题dp(i, W)为前i个物品中，选择的重量不超过W。对于第i个物品，要么不选；要没选，因此dp公式为：
dp(i, W) = max(dp(i-1, W), dp(i-1, W-Wi W_iW 
i
​	
 )+vi v_iv 
i
​	
 )

'''

def package_01(n, weights, values, C):
	dp = [[0]*(C+1) for _ in range(n+1)]
	for i in range(1, n+1):
		for j in range(1, C+1):
			dp[i][j] = dp[i-1][j]
			if j-weights[i-1] > 0:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
	from pprint import pprint
	pprint(dp)
	return dp[n][C]


n=5
c=10
w=[2,2,6,5,4]
v=[6,3,5,4,6]
print(package_01(n, w, v, c))
