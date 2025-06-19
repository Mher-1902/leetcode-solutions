class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ls = []
        fs = nums[0]
        count = 1
        for i in nums:
            if i - fs > k:
                count += 1
                fs = i
        return count