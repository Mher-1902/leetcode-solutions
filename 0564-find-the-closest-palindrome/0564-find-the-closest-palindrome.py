class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == "1":
            return "0"
        if n == "10":
            return "9"
        if n == "11":
            return "9"

        l = 0
        r = len(n) - 1
        m = (l + r) // 2
        left_half = n[l:m+1]

        if not left_half:
            left_half = n

        if len(n) % 2 == 0:
            mirror = left_half + left_half[::-1]
        else:
            mirror = left_half + left_half[:-1][::-1]

        minus_one = str(int(left_half) - 1)
        if len(minus_one) < len(left_half):
            minus_one_mirror = '9' * (len(n) - 1)
        else:
            if len(n) % 2 == 0:
                minus_one_mirror = minus_one + minus_one[::-1]
            else:
                minus_one_mirror = minus_one + minus_one[:-1][::-1]

        plus_one = str(int(left_half) + 1)
        if len(plus_one) > len(left_half):
            plus_one_mirror = '1' + '0' * (len(n) - 1) + '1'
        else:
            if len(n) % 2 == 0:
                plus_one_mirror = plus_one + plus_one[::-1]
            else:
                plus_one_mirror = plus_one + plus_one[:-1][::-1]

        int_n = int(n)
        candidates = [int(mirror), int(minus_one_mirror), int(plus_one_mirror)]
        candidates = [x for x in candidates if x != int_n]

        return str(min(candidates, key=lambda x: (abs(x - int_n), x)))
