class Solution(object):
    def findNumbers(self, nums):
        ls = []
        cnt = 0
        for i in nums:
            ls.append(str(i))
        for i in ls:
            if len(i) % 2 == 0:
                cnt += 1
        return cnt
        