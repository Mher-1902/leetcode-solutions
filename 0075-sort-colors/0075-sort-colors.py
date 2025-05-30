class Solution:
    def sortColors(self, nums: List[int]) -> None:
        max_val = max(nums)
        count = [0] * (max_val+1)
        for i in nums:
            count[i] += 1

        j = 0
        for k in range(len(count)):
            for _ in range(count[k]):
                nums[j] = k
                j += 1
        return nums

        