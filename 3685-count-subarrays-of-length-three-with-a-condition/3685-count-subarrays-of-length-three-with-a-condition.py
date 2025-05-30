class Solution(object):
    def countSubarrays(self, nums):
        return sum(b == (a + c) * 2
               for a, b, c in zip(nums, nums[1:], nums[2:]))
        