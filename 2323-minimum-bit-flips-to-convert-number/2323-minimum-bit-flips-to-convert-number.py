class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        b1 = bin(res)
        return b1.count('1')