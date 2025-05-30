class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        res = max(nums1)-max(nums2)
        if res < 0:
            res = res * (-1)
        else:
            res = res * (-1)
        return res
        