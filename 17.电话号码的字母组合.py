'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = [i for i in dic[digits[0]]]
        for i in digits[1:]:
            res = [m + n for m in res for n in dic[i]]
        return res
        
        # solution 2
        if not digits:
            return None
        self.dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return self.iter(digits)
    
    def iter(self, digits):
        temp = []
        if len(digits) == 0:
            return ['']
        else:
            for i in self.dic[digits[0]]:
                tmp = self.iter(digits[1:])
                for j in tmp:
                    temp.append(i + j)
        return temp

        # solution 3
        if not digits:
            return []
        type_dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [""]
        for d in digits:
            temp = []
            if d in type_dic.keys():
                for c in type_dic[d]:
                    for r in res:
                        temp.append(r + c)
                res = temp
        return res