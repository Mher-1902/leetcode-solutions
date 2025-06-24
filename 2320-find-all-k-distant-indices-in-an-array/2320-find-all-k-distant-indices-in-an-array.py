class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        for j in range(len(nums)):
            if nums[j] == key:
                for i in range(j-k,j+k+1):
                    if 0 <= i < len(nums):
                        res.add(i)
        return sorted(res)

        