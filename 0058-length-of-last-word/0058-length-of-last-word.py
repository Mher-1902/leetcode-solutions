class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       s = s.strip()
       ls = s.split()
       return len(ls[-1])