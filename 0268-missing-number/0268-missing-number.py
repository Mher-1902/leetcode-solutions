class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        ex = n * (n+1) // 2
        return ex - sum(nums)