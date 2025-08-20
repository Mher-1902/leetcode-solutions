class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        nums1.clear()
        nums1.extend(nums1_copy)
        nums1.extend(nums2)
        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums1)-i-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
                    flag = True
            if not flag:
                break
