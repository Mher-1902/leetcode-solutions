class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >= 1 and (sum(map(int,bin(n)[2:])) == 1):
            return True

        return False

        