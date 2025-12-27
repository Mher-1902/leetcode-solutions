import sys
sys.set_int_max_str_digits(20000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''.join(str(i) for i in num)
        s2 = str(int(s) + k)
        ls = [int(i) for i in s2]
        return ls

        