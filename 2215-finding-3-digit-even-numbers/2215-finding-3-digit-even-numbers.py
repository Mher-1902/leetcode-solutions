from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ls = []
        for num in range(100,1000,2):
            digits_in_num = list(map(int, str(num)))
            cnt2 = Counter(digits_in_num)
            if all(cnt2[i] <= cnt[i] for i in cnt2):
                ls.append(num)
        return sorted(ls)
