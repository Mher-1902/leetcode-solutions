import math
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        k = 3
        total = 0
        for j in range(0,k+1):
            sign = (-1) ** j
            cmb = math.comb(k,j)
            top = n - j * (limit + 1) + k -1
            if top >= 0:
                total += sign * cmb * math.comb(top,k-1)
        return total