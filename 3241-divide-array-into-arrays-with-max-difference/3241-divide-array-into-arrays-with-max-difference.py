class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ls = []
        res = []
        nums.sort()
        for i in range(0,len(nums),3):
            ls.append([nums[i],nums[i+1],nums[i+2]])
            i += 3
        for a,b,c in ls:
            if c - a <= k:
                res.append([a,b,c])
            elif c - a > k:
                return []
        return res

        