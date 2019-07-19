class Solution:
    def longestValidParentheses(self, s: str) -> int:
        动态规划
        dp = [0 for _ in range(len(s) + 1)] # 多+1 防止字符串为空
        for i in range(1, len(s)):
            if s[i] == ')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
        return max(dp)
        
        # 栈
        st = 0
        stack = []
        maxlen = 0
        for i in range(len(s)):
            if s[i] == '(':           #如果是左括号，直接入stack
                stack.append(i)
            else:                    #如果右括号
                if len(stack) == 0:  #如果stack里没有元素匹对，说明有效括号已经结束，更新起始位置
                    st = i + 1
                    continue
                else:                #有元素匹对
                    a = stack.pop()   #pop出一个左括号匹对
                    if len(stack) == 0:    #如果此时没了，不能保证不继续有效括号，所以根据当前的最长距离去更新maxlen
                        maxlen = max(i - st + 1, maxlen)
                    else:                 #如果此时还有 则计算与栈顶的索引相减来计算长度
                        maxlen = max(i - stack[-1], maxlen)
        return maxlen

        # 栈2
        stack = [-1]
        res = 0
        for i, x in enumerate(s):
            if x == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)          
        return res