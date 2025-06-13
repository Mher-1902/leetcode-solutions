class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls = [i**2 for i in nums]
        ls.sort()
        return ls
        