class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            l = r = 0
            ls = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ls.append(left[l])
                    l += 1
                else:
                    ls.append(right[r])
                    r += 1
            ls += left[l:]
            ls += right[r:]
            return ls
        return merge(nums)
        