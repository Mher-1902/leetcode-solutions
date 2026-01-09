class Solution:
    def mirrorDistance(self, n: int) -> int:
        def mirror(num):
            s = str(num)
            rev_s = ''.join(s[::-1])
            return int(rev_s)
        mirr_num = mirror(n)
        return abs(n - mirr_num)
        