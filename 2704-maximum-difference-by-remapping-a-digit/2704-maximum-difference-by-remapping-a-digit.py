class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        s1 = str(num)
        for i in s:
            if i != '9':
                s = s.replace(i,'9')
                break
        for i in s1:
            if i != '0':
                s1 = s1.replace(i,'0')
                break
        i1 = int(s)
        i2 = int(s1)
        return i1 - i2
                    
        