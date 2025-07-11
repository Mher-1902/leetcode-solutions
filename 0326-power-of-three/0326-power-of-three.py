class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n > 1:
            if n // 3 * 3 != n:
                return False
            n = n // 3
        return True