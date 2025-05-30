class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        sna = nums.copy()
        res = []
        res.extend(ans)
        res.extend(sna)
        return res