class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm < 0:
                    l += 1
                elif sm > 0:
                    r -= 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    r = r - 1
                    while l < r and nums[l] == nums[l-1]:
                            l += 1
                    while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return ans