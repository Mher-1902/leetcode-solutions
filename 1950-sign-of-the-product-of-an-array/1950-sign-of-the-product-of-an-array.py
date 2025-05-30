class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pr = 1
        for i in nums:
            pr *= i
        if pr > 0:
            return 1
        elif pr == 0:
            return 0 
        else:
            return -1

        