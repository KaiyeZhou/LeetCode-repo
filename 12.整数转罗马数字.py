class Solution:
    def intToRoman(self, num: int) -> str:
        # roman = ""
        # if num < 1 or num > 3999:
        #     return roman
        # # 千位数
        # m = num // 1000
        # roman = "M" * m
        # # 百位数
        # n = num % 1000 // 100
        # if n == 9:
        #     roman += "CM"
        # if 5 <= n < 9:
        #     roman += "D"
        #     roman += "C" * (n - 5)
        # if n == 4:
        #     roman += "CD"
        # if 1 <= n < 4:
        #     roman += "C" * n
        # # 十位数
        # n = num % 100 // 10
        # if n == 9:
        #     roman += "XC"
        # if 5 <= n < 9:
        #     roman += "L"
        #     roman += "X" * (n - 5)
        # if n == 4:
        #     roman += "XL"
        # if 1 <= n < 4:
        #     roman += "X" * n
        # # 个位数
        # n = num % 10
        # if n == 9:
        #     roman += "IX"
        # if 5 <= n < 9:
        #     roman += "V"
        #     roman += "I" * (n - 5)
        # if n == 4:
        #     roman += "IV"
        # if 1 <= n < 4:
        #     roman += "I" * n
        # return roman
        
        ### 2
#         M = ['', 'M', 'MM', 'MMM'] # 0,1000,2000,3000
#         C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 0,100,200,300,...,900
#         X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 0,10,20,30,...,90
#         I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 0,1,2,3,...,9
        
#         result = M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
#         return result
        
        ### 3
        roman = ""
        div = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        while num != 0:
            for i in range(len(div)):
                d = div[i]
                times = num // d
                if times != 0:
                    roman += romans[i] * times
                    num = num - d * times
        return roman

        ### 4
        rom = { 1000:'M', 900:'CM', 500:'D',400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL',
               10:'X', 9:'IX', 5:'V', 4: 'IV',1:'I'}
        output = ""
        for r in rom.keys():
            while r <= num:
                num -= r
                output += rom[r]
        return output