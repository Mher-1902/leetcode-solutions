class Solution(object):
    def isPalindrome(self, x):
        st = str(x)
        if x < 0:
            return False
        elif st[::-1] == st:
            return True
        elif st[::-1] != st:
            return False
        elif st[-1] == '0':
            return False
        