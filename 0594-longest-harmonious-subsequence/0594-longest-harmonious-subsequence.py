from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        lenght = 0
        for num in nums:
            if num + 1 in freq:
                curr_lenght = freq[num] + freq[num+1]
                lenght = max(curr_lenght,lenght)
        return lenght
        