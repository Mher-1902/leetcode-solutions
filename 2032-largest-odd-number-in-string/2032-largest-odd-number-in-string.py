class Solution:
    def largestOddNumber(self, num: str) -> str:
        ls = [int(i) for i in num]
        l = len(num)-1
        while ls[l] % 2 == 0:
                ls.pop(l)
                l -= 1
                if len(ls) == 0:
                        print('')
                        break
        res = ''
        for o in ls:
                res += str(o)
        return res
        