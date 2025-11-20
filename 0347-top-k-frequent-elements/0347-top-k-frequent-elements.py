class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls = []
        di = {}
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        for key,val in di.items():
            ls.append(val)
        ls.sort(reverse=True)
        trg = ls[:k]
        res = [k for k,v in di.items() if v in trg]
        return res  
        
