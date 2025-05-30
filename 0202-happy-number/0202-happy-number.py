class Solution(object):
    def isHappy(self, n):
        seen = []
        while n!=1:
            sm = sum(int(i)**2 for i in str(n))
            if sm in seen:
                return False
            seen.append(sm)
            n = sm
        return True
        
        