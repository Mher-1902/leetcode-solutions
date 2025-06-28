class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        orig = nums[:]
        idx = [[i,nums[i]] for i in range(len(nums))]
        nums.sort(reverse=True)
        ls = nums[:k]
        res = []
        for num in orig:
            if num in ls:
                res.append(num)
                ls.remove(num)
        return res

        

        