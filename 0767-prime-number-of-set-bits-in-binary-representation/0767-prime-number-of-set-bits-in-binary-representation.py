class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = [2, 3, 5, 7, 11, 13, 17, 19]
        ls = [bin(i) for i in range(left,right+1)]
        ls = [i.count('1') for i in ls]
        cnt = sum(1 for i in ls if i in res)       
        return cnt
        