class Solution(object):
    def removeDuplicates(self, nums):
        counts = 0
        for i in nums[:]:
            if nums.count(i) >= 2:
                counts += 1
                nums.remove(i)
        