class Solution(object):
    def finalString(self, s):
        s1 = ''
        for i in s:
            if i != 'i':
                s1 += i
            else:
                s1 = s1[::-1]
                s1 += i

        s1 = s1.replace('i','')
        return s1
        