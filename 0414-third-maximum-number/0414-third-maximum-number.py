class Solution(object):
    def thirdMax(self, nums):
        st = set(nums)
        if len(nums) <= 2:
            return max(nums)
        if len(st) < 3:
            return max(st)
        else:
            for i in nums:
                if nums.count(i) > 1:
                    nums.remove(i)
                    for j in nums:
                        if nums.count(j) > 1:
                            nums.remove(j)
            if len(nums) <= 2:
                return max(nums)
            else:
                nums.remove(max(nums))
                nums.remove(max(nums))
            return max(nums)