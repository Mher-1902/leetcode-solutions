class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = set(nums1)
        st2 = set(nums2)
        ls = []
        for i in st:
            if i in st2:
                ls.append(i)
        return ls

        