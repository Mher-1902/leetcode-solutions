class Solution:
    def reverseVowels(self, s: str) -> str:
        l_vowls = ['a', 'e', 'i', 'o','u']
        u_vowls = ['A', 'E', 'I', 'O','U']
        l = 0
        r = len(s)-1
        s = list(s)
        while l < r:
            if (s[l] in l_vowls or s[l] in u_vowls) and (s[r] in l_vowls or s[r] in u_vowls):
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
            elif s[l] not in l_vowls and s[l] not  in u_vowls:
                l += 1
            elif s[r] not in l_vowls and s[r] not in u_vowls:
                r -= 1
        s = ''.join(s)
        return s
        