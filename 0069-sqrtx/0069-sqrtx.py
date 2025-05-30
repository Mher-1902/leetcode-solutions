class Solution:
    def mySqrt(self, x: int) -> int:
        L,R = 1,x
        while L <= R:
            M = (L+R) // 2
            M_squered = M * M
            if x == M_squered:
                return M
            elif x > M_squered:
                L = M + 1
            else:
                R = M - 1
        return R