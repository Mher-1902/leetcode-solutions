class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ls = []
        ans = abs(nums[0] - nums[-1])
        for i in range(len(nums)):
            diff = abs(nums[i] - nums[i-1])
            ans = max(ans,diff)
        return ans


            
        