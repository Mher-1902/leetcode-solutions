class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for i in nums[1:]:
            if i > min_val:
                max_diff = max(max_diff,i-min_val)
            else:
                min_val = i
        return max_diff