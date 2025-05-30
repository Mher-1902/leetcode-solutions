class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ls = [int(i) for i in str(n)]
        res1 = 1
        res2 = sum(ls)
        for i in ls:
            res1 *= i
        res = res1 - res2
        return res
        