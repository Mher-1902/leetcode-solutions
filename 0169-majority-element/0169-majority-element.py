from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = Counter(nums)
        max_key = None
        max_val = 0
        for a,b in di.items():
            if b > max_val:
                max_val = b
                max_key = a
        return max_key
        