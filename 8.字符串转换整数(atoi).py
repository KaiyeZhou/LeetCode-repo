class Solution:
    def myAtoi(self, str: str) -> int:
        # if len(str) == 0 or len(str.strip()) == 0:
        #     return 0
        # s = str.lstrip()
        ### 1
#         res = []
#         flag = True      ##一旦有整数字符出现，则标记为False
#         numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
#         for i in range(len(str)):
#             if str[i] == ' ' and flag:
#                 continue
#             if str[i] == '+' and flag:     # 如果+字符第一次出现，则添加到列表中，标记修改为False并继续
#                 res.append(str[i])
#                 flag = False
#                 continue
#             if str[i] == '-' and flag:
#                 res.append(str[i])
#                 flag = False
#                 continue
#             if str[i] not in numList:
#                 break
#             else:
#                 res.append(str[i])
#                 flag = False
#         res = ''.join(res)
#         if res == '+' or res == '-' or res == '':
#             return 0
#         else:
#             res = int(res)
#         if res > 2**31-1:
#             return 2**31-1
#         if res < -2**31:
#             return -2**31
#         else:
#             return res
        
        ### 2
        s = str.strip()
        res = []
        if len(s) == 0:
            return 0
        if s[0] == '+':
            res += s[0]
        elif s[0] == '-':
            res += s[0]
        elif s[0] >= '0' and s[0] <= '9':
            res += s[0]
        else:
            return 0
        for i in range(1, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                res += s[i]
            else:
                break
        res = ''.join(res)    # 拼接字符串
        if len(res) == 0 or (len(res) == 1 and (res[0] == '+' or res[0] == '-')):
            return 0
        res = int(res)
        if res > 2**31-1:
            return 2**31-1
        if res < -2**31:
            return -2**31
        return res