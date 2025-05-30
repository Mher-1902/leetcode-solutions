class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st1 = set(nums1)
        st2 = set(nums2)
        ls1 = list(st1-st2)
        ls2 = list(st2-st1)
        return [ls1,ls2]
        