class Solution(object):
    def separateDigits(self, nums):
        st = ''
        ls = []
        for i in nums:
            st = st + str(i)
        for j in st:
            ls.append(int(j))
        return ls
        