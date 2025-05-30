class Solution(object):
    def differenceOfSum(self, nums):
        smn = sum(nums)
        ls = []
        srt = ''
        for i in nums:
            srt += str(i)
        for i in srt:
            ls.append(int(i))
        smn2 = sum(ls)
        return smn-smn2