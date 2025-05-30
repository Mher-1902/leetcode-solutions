import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        r = 0
        ls = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                ls.append(nums1[l])
                l += 1
            else:
                ls.append(nums2[r])
                r += 1
        while l < len(nums1):
            ls.append(nums1[l])
            l += 1
        while r < len(nums2):
            ls.append(nums2[r])
            r += 1
        arr = np.array(ls)
        return float(np.median(arr))
        